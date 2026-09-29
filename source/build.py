"""Build the supplement while preserving the original archival body."""
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

import pymupdf

from analyze import analyze

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'archive/extended_methods_and_results_20260927.pdf'
ARCHIVE_SHA256 = '0c73972904defcb68b79dedc5f505b9166c5bb8b75c3202c52dcf5bbcae95ef1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sanitized(doc, title):
    doc.set_metadata({'title': title, 'author': '', 'subject': '', 'keywords': '',
                      'creator': '', 'producer': '', 'creationDate': '', 'modDate': ''})
    doc.del_xml_metadata()


def main():
    analysis = analyze()
    assert sha(ARCHIVE) == ARCHIVE_SHA256, 'Archived source changed'
    with tempfile.TemporaryDirectory(prefix='supplement-build-') as tmp:
        output = Path(tmp)
        for stem in ('cover', 'addendum'):
            command = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                       f'-output-directory={output}', f'{stem}.tex']
            for _ in range(2):
                run = subprocess.run(command, cwd=ROOT / 'source',
                                     capture_output=True, text=True)
                if run.returncode:
                    raise RuntimeError(run.stdout[-6000:] + run.stderr)
            log = (output / f'{stem}.log').read_text()
            assert 'Overfull' not in log, f'Layout overflow in {stem}'

        archive = pymupdf.open(ARCHIVE)
        cover = pymupdf.open(output / 'cover.pdf')
        addendum = pymupdf.open(output / 'addendum.pdf')
        assert len(archive) == 32 and len(cover) == 1
        sanitized(addendum, 'Supplementary Clarifications and Paired-Outcome Accounting')
        addendum.save(ROOT / 'supplement_addendum.pdf', garbage=4, deflate=True)

        combined = pymupdf.open()
        combined.insert_pdf(cover)
        combined.insert_pdf(archive, from_page=1)
        combined.insert_pdf(addendum)
        combined.set_toc([
            [1, 'Navigation and update scope', 1],
            [1, 'Archival bibliography and Appendices A–F', 2],
            [2, 'A. Historical agent studies', 3],
            [2, 'B. Corpus, retrieval, and execution', 7],
            [2, 'C. Earlier repair protocols', 12],
            [2, 'D. Common-prompt context study', 20],
            [2, 'E. Inventory and serialization', 25],
            [2, 'F. Source review', 29],
            [1, 'S1–S6. Clarifications and paired-outcome accounting', 33],
        ])
        sanitized(combined, 'Extended Methods and Results — When Valid Evidence Goes Unused in Oncology Agents')
        destination = ROOT / 'extended_methods_and_results.pdf'
        combined.save(destination, garbage=4, deflate=True)
        combined.close()
        final = pymupdf.open(destination)
        for i in range(1, 32):
            assert archive[i].get_text() == final[i].get_text(), f'Text changed on PDF page {i+1}'
            assert archive[i].get_pixmap().samples == final[i].get_pixmap().samples, f'Render changed on PDF page {i+1}'
        for key in ('author', 'creator', 'producer', 'creationDate', 'modDate'):
            assert not final.metadata.get(key), key
        assert final.embfile_count() == 0
        stats = {
            'archive_sha256': sha(ARCHIVE),
            'extended_pdf_sha256': sha(destination),
            'addendum_pdf_sha256': sha(ROOT / 'supplement_addendum.pdf'),
            'combined_pages': len(final), 'addendum_pages': len(addendum),
            'addendum_starts_at_pdf_page': 33,
            'archival_body_pages_render_and_text_equal': 31,
            'identifying_pdf_metadata_empty': True,
            'embedded_files': final.embfile_count(),
            'paired_data_sha256': analysis['data_sha256'],
            'new_model_calls': 0,
        }
        (ROOT / 'data/verification.json').write_text(json.dumps(stats, indent=2) + '\n')
        print(json.dumps(stats, indent=2))


if __name__ == '__main__':
    main()
