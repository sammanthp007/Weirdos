(define (equalsimp n m)
  (cond
    ((null? n) (null? m))
    ((null? n) #F)
    ((eq? (car n) (car m))
     (equalsimp (cdr n) (cdr m)))
    (else #F)
    )
  )

(equalsimp '(A B C) '(A B C))
