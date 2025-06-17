export interface ReviewState {
  interval: number; // days
  easeFactor: number;
  repetitions: number;
}

export interface ReviewResult extends ReviewState {}

/**
 * Calculate next spaced repetition values using the SM-2 algorithm.
 * @param state Previous review state
 * @param quality Response quality from 0 to 5
 */
export function sm2(state: ReviewState, quality: number): ReviewResult {
  let { interval, easeFactor, repetitions } = state;

  if (quality < 3) {
    repetitions = 0;
    interval = 1;
  } else {
    if (repetitions === 0) {
      interval = 1;
    } else if (repetitions === 1) {
      interval = 6;
    } else {
      interval = Math.round(interval * easeFactor);
    }
    repetitions += 1;
  }

  easeFactor = easeFactor + 0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02);
  if (easeFactor < 1.3) {
    easeFactor = 1.3;
  }

  return { interval, easeFactor, repetitions };
}
