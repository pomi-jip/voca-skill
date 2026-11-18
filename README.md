# vocab-skill

> 영문 수업 자료(PDF, DOCX, PPTX, TXT)를 업로드하면 중요 단어를 추출해 단어장(마크다운 + HWPX)을 자동 생성하는 AI 에이전트 스킬

## 지원 에이전트

- ✅ Google Antigravity (AGY / agy CLI)
- ✅ Claude Code
- ✅ OpenAI Codex

## 기능

- 파일에서 중요 어휘 자동 선별 (강조 단어 우선 + AI 추가 선별)
- 영어 단어 + 한국어 뜻 + 품사 + 예문 정리
- 마크다운 단어장 & 한글 HWPX 단어장 동시 생성
- 지원 형식: PDF, DOCX, PPTX, TXT

## 설치 방법

```bash
# AGY (Antigravity CLI)
git clone https://github.com/pomi-jip/voca-skill.git ~/.gemini/config/skills/vocab-skill

# Claude Code
git clone https://github.com/pomi-jip/voca-skill.git ~/.claude/skills/vocab-skill

# OpenAI Codex
git clone https://github.com/pomi-jip/voca-skill.git ~/.codex/skills/vocab-skill
```

## 의존 패키지 설치 (선택)

```bash
python -m pip install -r requirements.txt
```

> PDF, DOCX, PPTX 파일 추출 시 필요. TXT는 패키지 없이 동작.

## 사용법

에이전트에서 영문 수업 파일을 업로드한 뒤:

> "이 파일에서 단어장 만들어줘"

## 라이선스

MIT
