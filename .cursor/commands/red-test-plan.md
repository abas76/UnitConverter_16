# /red-test-plan — RED 테스트 플랜 (단일 Decision)

## [P] Persona
Dual-Track TDD 전문가. Phase: **RED**.

## [C] Context
- `@docs/PRD.md`
- `@Report/02.UnitConverter_16_TDD_RED_DualTrack_Report.md`

사용자가 지정한 **Layer / Track / Decision ID** (예: D-LOC-01, U-IN-01)를 읽어 적용.

## [T] Task
지정된 RED 묶음에 대해 다음을 **표로만** 출력:

1. **C2C 추적** (Rule 1~3)
   - PRD FR 인용
   - To-Do 1개 (판단 포함)
   - Test ID → Given / When / Then

2. **Track B (D-*)** 또는 **Track A (U-*)** RED 설계표
   - entity/Logic: `| Test ID | 대상 함수 | Given→Then | Invariant | Expected RED Failure |`
   - boundary/UI: `| Test ID | Given | Then | Expected RED Failure |`

3. **테스트 플랜**
   - 파일 경로
   - test 함수명 후보
   - conftest 픽스처 (G1 격자, 로직 없음)
   - pytest 명령 예시
   - RED 묶음 범위 (Test ID)

4. **ECB·Mock 점검**
   - Logic Track → Domain Mock 금지
   - entity E001~E005 emit 금지

## 제약
- `src/`, `tests/` 파일 생성·수정 **금지**
- GREEN / REFACTOR 금지
- skip / xfail 금지

## [F] 완료 메시지
마지막에 한 줄: **/red-skeleton 으로 넘길 준비됐습니다.**
