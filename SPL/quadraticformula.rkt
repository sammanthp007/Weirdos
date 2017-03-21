(define (quadroot a b c)
  (let
      (
       (minus_b_over_2a (/ (- 0 b) (* 2 a)))
       (root_part (/ (sqrt (- (* b b) (* 4 a c))) (* 2 a)))
       )
    (display (+ minus_b_over_2a root_part))
    (newline)
    (display (- minus_b_over_2a root_part))
    )
  )

(quadroot 1 5 6)
