(define (reverse-simple l)
  (cond
    ((null? l) '())
    ((not (list? l)) (car l))
    (else (append (reverse-general (cdr l)) (list (car l))))
    )
  )

(reverse-simple '(a b c))
