#lang racket
;Ejercicio 1
(write "Ejercicio 1 ")
(newline)
(define (funcion n m)
  (cond
  [(= m 0) 0]
  [(= n 0) (* 2 m)]
  [(= m 1) 2]
  [else (funcion (- n 1) (funcion n (- m 1) ) )]))

(funcion 1 10)
(funcion 2 4)
(funcion 3 3)





;Ejercicio 2
(write "Ejercicio 2 Recursivo")
(newline)

(define (collatz n)

    (cond
    [(= n 1) 0]
    [(even? n)  (+ (collatz(/ n 2)) 1)]
    [else (+ (collatz(+ 1 (* 3 n))) 1)]))



(collatz 16)

(collatz 12)

(collatz 31)


(write "Ejercicio 2 Recursivo Lineal")
(newline)
(define (collatz2 n)
  (iter-collatz 0 n))

(define (iter-collatz  i n)
  (cond
    [(= n 1) i]
    [(even? n) (iter-collatz (+ i 1)  (/ n 2))]
    [else (iter-collatz (+ i 1) (+ 1 ( * 3 n)))]
    ))

(collatz2 16)

(collatz2 12)

(collatz2 31)





(write "Ejercicio 3 Recursivo ")
(newline)

(define (func1 n)
  (cond
    [(= n 0) 1]
    [(= n 1) 0]
    [(= n 2) -1]
    [else (- (* 2 (func1 (- n 1))) (* 7(func1(- n 2))) (* 6 (func1(- n 3))) )])

  )

(func1 4)
(func1 12)
(func1 23)

(write "Ejercicio 3 Recursivo Lineal")
(newline)
(define (func1-iter1 n)
  (func1-iter 0 -1 1 1 n)
  )

(define (func1-iter ant res trasante i n)
  (if(>= i n)
     ant
     (func1-iter res (- (* 2 res) (* 7 ant) (* 6 trasante)) ant (+ i 1) n
      )
     )
  )
(func1-iter1 4)
(func1-iter1 12)
(func1-iter1 23)



(write "Ejercicio 4 Normal")
(newline)

(define (productoria1 a n)
  (if (> a n)
      1
      (* (* ( + (* a a a ) (* 7 a) -11) ( + (* a a a ) (* 7 a) -11) )
         (productoria1(+ a 1) n)) ))
(productoria1 1 2)

(write "Ejercicio 4 Termino")
(newline)


(define (productoria f a n)
  (if (> a n)
      1
      (* (f a) (productoria f (+ a 1) n) )))



(define (cuadrado n)
  (* n n))

(define(cubo n)
  (* n n n))

(define (termino i)
  (cuadrado ( + (cubo i) (* 7 i) -11)))

(define (serie1 a n)
  (productoria termino a n))
;aaa

(serie1 1 2)
  

(define (productoria2 a n)
  (productoria  (lambda (i)(cuadrado ( + (cubo i) (* 7 i) -11)) ) a n  ) )



(write "Ejercicio 4 Lambda")
(newline)

(productoria2 1 2)

;Ejercicio 5
