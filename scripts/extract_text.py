#!/usr/bin/env python3
"""
extract_text.py — vocab-skill 텍스트 추출기
지원 형식: PDF, DOCX, PPTX, TXT
"""

import argparse
import sys
from pathlib import Path


def extract_pdf(path: Path) -> str:
    try:
        import pdfminer.high_level as pdfminer
        return pdfminer.extract_text(str(path))
    except ImportError:
        pass
    try:
        import pypdf
        reader = pypdf.PdfReader(str(path))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except ImportError:
        pass
    sys.exit("PDF 추출 실패: pdfminer.six 또는 pypdf 패키지를 설치하세요.\n  pip install pdfminer.six")


def extract_docx(path: Path) -> str:
    try:
        import docx
        doc = docx.Document(str(path))
        parts = []
        for para in doc.paragraphs:
            # 볼드/이탤릭 표시를 **로 변환
            line = ""
            for run in para.runs:
                text = run.text
                if run.bold:
                    text = f"**{text}**"
                elif run.italic:
                    text = f"*{text}*"
                line += text
            parts.append(line)
        # 표 내용도 추출
        for table in doc.tables:
            for row in table.rows:
                parts.append(" | ".join(cell.text for cell in row.cells))
        return "\n".join(parts)
    except ImportError:
        sys.exit("DOCX 추출 실패: python-docx 패키지를 설치하세요.\n  pip install python-docx")


def extract_pptx(path: Path) -> str:
    try:
        from pptx import Presentation
        prs = Presentation(str(path))
        parts = []
        for slide_num, slide in enumerate(prs.slides, 1):
            parts.append(f"\n--- Slide {slide_num} ---")
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for para in shape.text_frame.paragraphs:
                    line = ""
                    for run in para.runs:
                        text = run.text
                        if run.font.bold:
                            text = f"**{text}**"
                        elif run.font.italic:
                            text = f"*{text}*"
                        line += text
                    if line.strip():
                        parts.append(line)
        return "\n".join(parts)
    except ImportError:
        sys.exit("PPTX 추출 실패: python-pptx 패키지를 설치하세요.\n  pip install python-pptx")


def extract_txt(path: Path) -> str:
    for enc in ("utf-8", "utf-8-sig", "cp949", "euc-kr", "latin-1"):
        try:
            return path.read_text(encoding=enc)
        except (UnicodeDecodeError, LookupError):
            continue
    sys.exit(f"TXT 인코딩 감지 실패: {path}")


EXTRACTORS = {
    ".pdf": extract_pdf,
    ".docx": extract_docx,
    ".pptx": extract_pptx,
    ".txt": extract_txt,
    ".md": extract_txt,
}


def main():
    parser = argparse.ArgumentParser(description="수업 자료 파일에서 텍스트 추출")
    parser.add_argument("--input", "-i", required=True, help="입력 파일 경로")
    parser.add_argument("--output", "-o", help="출력 파일 경로 (없으면 stdout)")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        sys.exit(f"파일 없음: {path}")

    ext = path.suffix.lower()
    if ext not in EXTRACTORS:
        sys.exit(f"지원하지 않는 형식: {ext}\n지원: {', '.join(EXTRACTORS)}")

    text = EXTRACTORS[ext](path)

    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"추출 완료: {args.output} ({len(text):,}자)")
    else:
        print(text)


if __name__ == "__main__":
    main()
