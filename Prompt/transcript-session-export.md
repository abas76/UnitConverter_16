# UnitConverter_16 — Session Transcript Export

> AI 협업 세션 기록 (요약·인용)  
> 프로젝트: UnitConverter_16 | 기간: 2026-06-11

---

## 세션 목차

1. [TDD · Mom Test 개요](#1-tdd--mom-test-개요)
2. [Mom Test 질문·프롬프트·시뮬레이션](#2-mom-test-질문프롬프트시뮬레이션)
3. [문제 정의 · PRD · 세션3 워크북](#3-문제-정의--prd--세션3-워크북)
4. [Mom Test 채점](#4-mom-test-채점)
5. [GitHub 업로드 · 브랜치 분리](#5-github-업로드--브랜치-분리)
6. [TDD RED Dual-Track 설계](#6-tdd-red-dual-track-설계)
7. [RED Skeleton (D-LOC-01)](#7-red-skeleton-d-loc-01)
8. [저장 산출물 목록](#8-저장-산출물-목록)

---

## 1. TDD · Mom Test 개요

**사용자 요청:** TDD, Mom Test 목적과 방법 간략 설명

**핵심 응답:**
- **TDD:** Red → Green → Refactor. 테스트 = 실행 가능한 명세서
- **Mom Test:** 과거 행동·구체적 사례. "좋은 아이디어네요" 거짓 피드백 제거
- **Unit Converter 적용:** 변환기 존재가 아니라 **신뢰·재확인 비용** 해결

---

## 2. Mom Test 질문·프롬프트·시뮬레이션

### 생성 프롬프트
- `Prompt/mom-test-interview-prompt.md`
- `Prompt/mom-test-simulation-prompt.md`
- `Prompt/mom-test-questions.md`

### 역할 분리 시뮬레이션 [시뮬레이션]

**페르소나:** 프로그래밍 수업 UnitConverter 과제 학생

**Turn 1~3 요약:**
- 해외 직구: inch ↔ cm 변환 필요
- 구글·네이버 결과 소수점 불일치 → 2.54 직접 재계산
- 리뷰 사진으로 교차 확인 후 구매

**표면 문제:** "변환 프로그램을 만든다"  
**진짜 문제:** 출처별 결과 불일치 → 재계산·교차 확인 → 시간·판단 흔들림

**증거 3줄:**
1. "소수점 자리가 조금 달라서 헷갈렸어요"
2. "2.54를 직접 곱해 봤습니다"
3. "리뷰 사진 보면서 대략적인 크기 감 잡고"

---

## 3. 문제 정의 · PRD · 세션3 워크북

### 진짜 문제 → R-G-I-O

| 항목 | 내용 |
|------|------|
| 주제 | 한 입력 → meter/feet/yard 일관 출력 + 잘못된 입력 차단 |
| Role | 일관된 변환 결과 보장 개발자 |
| Goal | 수동 재계산·교차 확인 없이 신뢰 가능한 전 단위 결과 |
| Input | `단위:값` (meter/feet/yard) |
| Output | 전 단위 결과 + 명확한 오류 |

### 생성 문서
- `Report/01.UnitConverter_16_ProblemDefinition_Report.md`
- `docs/PRD.md`

---

## 4. Mom Test 채점

**점수: 8/10**

| 체크 | 결과 |
|------|------|
| 미래 가정 없음 | ✅ |
| 과거 행동 구체성 | ✅ |
| 진짜 문제 솔루션名 없음 | ✅ |
| 표면/진짜 분리 | ✅ |
| UnitConverter 도메인 | △ |

**고칠 질문:** "meter, feet, yard가 섞인 자료를 본 적 있나요?"

---

## 5. GitHub 업로드 · 브랜치 분리

**저장소:** https://github.com/abas76/UnitConverter_16

| 브랜치 | 내용 |
|--------|------|
| main | 기본 프로젝트 (README, UnitConverter.py, unit-converter.jpg) |
| spec | Mom Test · Report · PRD 전체 |

**머지 없이** 브랜치 분리 업로드 완료.

---

## 6. TDD RED Dual-Track 설계

### `/red-test` — FR-01~03

| Track | ID | 범위 |
|-------|-----|------|
| A | U-IN-01~05 | 입력 시나리오 |
| A | U-OUT-01 | 전 단위 출력 |
| A | U-FLOW-02 | E2E |
| B | D-LOC-01 | `parse_unit_value` / `find_blank_coords` |
| B | D-CONV-01 | `to_meter_base` |
| B | D-EMIT-01 | `convert_to_all_units` |

### `/red-test-plan` — D-LOC-01 (entity/Logic)

| Test ID | Given | Then |
|---------|-------|------|
| T-D-LOC-01-01 | `meter:2.5` / G1 grid | `(meter, 2.5)` / `[(2,2),(3,3)]` |
| T-D-LOC-01-02 | `meter2.5` / no colon | `InvalidFormatError` |
| T-D-LOC-01-03 | `feet:8:2` | `(feet, 8.2)` |

### boundary/UI — U-IN-01, U-IN-02

| Test ID | Given | Expected RED |
|---------|-------|--------------|
| T-U-IN-01 | `meter:2.5`, grid=None | `ModuleNotFoundError` / E003 |
| T-U-IN-02 | `feet:8.2` | `AttributeError` |

### Cursor Commands 생성
- `.cursor/commands/red-test.md`
- `.cursor/commands/red-test-plan.md`

---

## 7. RED Skeleton (D-LOC-01)

### `/red-skeleton` 실행

| 항목 | 값 |
|------|-----|
| Phase | red |
| Layer | entity |
| Track | Logic |
| 파일 | `tests/entity/test_d_loc_01.py` |
| 픽스처 | `tests/conftest.py` — `grid_g1` (G1, 0이 2개) |
| 상수 | `GRID_WIDTH=34`, `GRID_HEIGHT=16`, `G1_GRID_SIZE=4` |

### pytest 실행

```bash
python -m pytest tests/entity/test_d_loc_01.py::test_d_loc_01_blank_coords_row_major -v
```

**결과:**
- exit code: **4**
- `ModuleNotFoundError: No module named 'src'`
- `src/` 미수정 규칙 준수 → collection error (RED 예상)

### 스켈레톤 규칙 준수

| 규칙 | 결과 |
|------|------|
| AAA 주석 | ✅ |
| `pytest.fail` only | ✅ |
| assert / skip / xfail 없음 | ✅ |
| src/ 미수정 | ✅ |

---

## 8. 저장 산출물 목록

### Report/
| 파일 | 설명 |
|------|------|
| `01.UnitConverter_16_ProblemDefinition_Report.md` | Mom Test 문제 정의 |
| `02.UnitConverter_16_TDD_RED_DualTrack_Report.md` | Dual-Track RED 설계 |
| `03.UnitConverter_16_RED_Skeleton_Report.md` | RED Skeleton + pytest 보고 |
| `mom-test-simulation-report.md` | 3턴 인터뷰 전문 |
| `mom-test-interview-conclusion.md` | 인터뷰 종료 요약 |
| `tdd-mom-test-overview.md` | TDD·Mom Test 개요 |

### Prompt/
| 파일 | 설명 |
|------|------|
| `mom-test-interview-prompt.md` | 인터뷰어 프롬프트 |
| `mom-test-simulation-prompt.md` | 시뮬레이션 프롬프트 |
| `mom-test-questions.md` | Mom Test 질문 목록 |
| `transcript-session-export.md` | 본 Transcript |

### tests/ (RED Skeleton)
| 파일 | 설명 |
|------|------|
| `conftest.py` | `grid_g1` 픽스처 |
| `entity/test_d_loc_01.py` | D-LOC-01 RED 3함수 |

### docs/
| 파일 | 설명 |
|------|------|
| `PRD.md` | 제품 요구사항 명세 |

---

## 사용자 프롬프트 타임라인 (요약)

| # | 사용자 요청 |
|---|------------|
| 1 | TDD Mom Test 목적·방법 설명 |
| 2 | Unit Converter Mom Test 질문 |
| 3 | Mom Test 인터뷰 프롬프트 |
| 4 | 역할 분리 시뮬레이션 3턴 |
| 5 | 인터뷰 종료 요약 |
| 6 | Mom Test 채점 |
| 7 | 세션3 워크북 |
| 8 | Report + PRD 생성 |
| 9 | GitHub 업로드 |
| 10 | 머지 해제 방법 |
| 11 | 브랜치 분리 업로드 |
| 12 | `/red-test-plan` D-LOC-01 |
| 13 | `/red-test` 커맨드 |
| 14 | `/red-test` 실행 |
| 15 | `/red-test-plan` |
| 16 | U-IN-01/02 boundary RED |
| 17 | Report + Transcript Export (1차) |
| 18 | `/red-skeleton` D-LOC-01 |
| 19 | Report + Transcript Export (2차) |

---

**[Transcript Export 종료]**
