(define (appendd n m)
  (cond
    ((null? n) m)
    (else
     (cons (car n) (appendd (cdr n) m))
     )
    )
  )

(appendd '(a b c) '(d e f))
