import { sm2, ReviewState } from '../src';

describe('sm2', () => {
  it('increments repetition and interval for good quality', () => {
    const state: ReviewState = { interval: 1, easeFactor: 2.5, repetitions: 1 };
    const result = sm2(state, 5);
    expect(result.repetitions).toBe(2);
    expect(result.interval).toBe(6);
    expect(result.easeFactor).toBeGreaterThan(state.easeFactor);
  });

  it('resets repetition on low quality', () => {
    const state: ReviewState = { interval: 10, easeFactor: 2.5, repetitions: 5 };
    const result = sm2(state, 2);
    expect(result.repetitions).toBe(0);
    expect(result.interval).toBe(1);
  });
});
