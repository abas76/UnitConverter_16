# /red-test — Dual-Track RED 테스트 설계표 생성

## [P] Persona
당신은 **Dual-Track TDD** 전문가입니다. 현재 phase는 **RED**입니다.
- Track A(Use Case): 사용자 관점 입·출력·흐름
- Track B(Domain/Logic): entity 계층 핵심 도메인 함수
- GREEN/REFACTOR·src/ 구현·tests/ 파일 생성은 **금지**
- 출력은 **설계표 Markdown 텍스트만**

## [C] Context
반드시 참조:
- `@docs/PRD.md` — FR·BR·입출력 명세
- `@.cursorrules` — `tdd_rules`, `architecture` (없으면 PRD §5·§6·§7 기본 적용)

프로젝트: **UnitConverter_16** — `단위:값` CLI 길이 변환 (meter / feet / yard)

## [T] Task
`FR-01`~`FR-03` 기반 **Dual-Track RED 설계표**를 작성하세요.

### Track A — Use Case (RED)
| ID | 범위 |
|----|------|
| U-IN-01 ~ U-IN-05 | 입력 파싱·검증 시나리오 (FR-1, §7 오류 명세) |
| U-OUT-01 | 한 입력 → 전 단위 출력 (FR-3) |
| U-FLOW-02 | CLI end-to-end 흐름 (입력→파싱→변환→출력) |

### Track B — Domain (RED)
핵심 도메인 함수 **3개** (D-XXX-01~03):
| Decision ID | FR 연결 | 함수(예상 경로) |
|-------------|---------|----------------|
| D-LOC-01 | FR-1 | `src.entity.input_parser.parse_unit_value` |
| D-CONV-01 | FR-2 | `src.entity.converter.to_meter_base` |
| D-EMIT-01 | FR-3 | `src.entity.converter.convert_to_all_units` |

### C2C Rule
1. Test 1개 = 판단 1개 (FR/Decision 추적)
2. Given/When/Then은 PRD에서 관측 가능한 항목만
3. Test ID → PRD FR/BR 역추적 가능

### 제약
- `src/`, `tests/` **파일 생성·수정 금지**
- skip / xfail 금지
- Logic Track → **Domain Mock 금지**
- entity E001~E005 **emit(print/log) 금지**
- 설계표만 출력

## [F] Format
아래 섹션을 **Markdown 표**로 출력:

### 1. C2C 추적
- PRD FR-01~03 인용
- To-Do 1개 (판단 포함)
- Test ID → Given / When / Then

### 2. Track A — Use Case RED 설계표
| Test ID | UC ID | Given | When | Then | Expected RED Failure |

### 3. Track B — Domain RED 설계표
| Test ID | Decision ID | 대상 함수 | Given→Then | Invariant | Expected RED Failure |

### 4. ECB·Mock 점검
| 항목 | Pass/Fail | 비고 |

### 5. RED 묶음 요약
- 범위 FR / Test ID 개수
- 다음 단계: `/red-test-plan` 또는 `/red-skeleton`

## 추가 인자
사용자가 `/red-test D-LOC-01` 처럼 Decision을 지정하면 해당 Decision만 상세화.
미지정 시 FR-01~03 전체 Dual-Track 표 출력.
