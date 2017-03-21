(define (equal n m)
  (cond
    ((not (list? n)) (eq? n m))
    ((not (list? m)) #F)
    ((null? n) (null? m))
    ((null? m) #F)
    ((equal (car n) (car m)) (equal (cdr n) (cdr m)))
    (else #F)
    )
  )

(equal '(A (b c) d ((e))) '(A (b c) d ((e))))
