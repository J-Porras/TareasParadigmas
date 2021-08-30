#lang racket
;Ejercicio 1

(define (porcen-vector lista x)
  (if  (null? lista)
       0
       (if (<= (car lista) x)
           (+ 1 (porcen-vector (cdr lista) x))
            (porcen-vector (cdr lista) x)
           )
       
       )
  )

(write "Ejercicio 1")
(newline)
(porcen-vector (list 3 3 3 3 3 3 10 10 10 10) 3)
(porcen-vector (list 2 2 3 4 5 6) 1)
(porcen-vector (list 1 2 3 4 5 6) 4)

;Ejercicio 2 a
(define (aplica-funcion fun L)
(if (null? L) '()
(cons (fun (car L)) (aplica-funcion fun (cdr L)))))





;Ejercicio 2 b
(define (ordena lista)
  (cond
    ((or (null? lista)  (null? (cdr lista))) 
     lista
     )
    (else
      (let (
            (pivote (car lista)) ; Primer elemento como pivote
            (resto (cdr lista))
            )
        (append
          (ordena ; ordena los valores menores que el pivote
            (filter (lambda (x) (< x pivote)) resto)
            ) ; retorna lista de valores menores que el pivote
          (list pivote) ; Lista con el pivote
          (ordena ; ordena los valores menores que el pivote
            (filter (lambda (x) (>= x pivote)) resto))
          )
        
        )
      )

    )
  ) 

(write "Ejercicio 2 b")
(newline)
(ordena (list  9 8 7 6 5 4 3 2 1))

(ordena (list  55 66 44 88 77 33 22 11 10))
(ordena (list  90 48 7 6 500 4 333 2 100))

;Ejercicio 2 c
(define (pega L1 L2)
(if (null? L1)
    L2
(cons (car L1) (pega (cdr L1) L2))))

(define (suma-tres L1 L2 L3)
  (pega L1 (pega L2 L3))
  )



(write "Ejercicio 2 c")
(newline)
(suma-tres (list 1 2 3) (list 4 5 6) ( list 7 8 9))

(suma-tres (list 1 2 3) '() ( list 7 8 9))

(suma-tres '() (list 11 22 33) ( list  120 70 80))
;Ejercicio 2 d

(define (subconjunto? lista1 lista2)
        (cond
            [(null? lista1 ) #t]
            [(null? lista2)#f]
            [(= (car lista1) (car lista2)) (subconjunto? (cdr lista1) (cdr lista2))]
            [else (subconjunto?  lista1 (cdr lista2))]
            )
  )

(write "Ejercicio 2 d")
(newline) 
(subconjunto? '(1 2 3) '( 5 1 2 8 7 3 9))
(subconjunto? '(1 2 3) '( 5 1 8 7 3 9))
(subconjunto? '( 6 8 7 1 3 9) '( 5 1 3 9))



;Ejercicio 2 e

(define eliminar
  (lambda (x lista)
    (cond
     ((equal? x (car lista)) (cdr lista))
     (else (cons (car lista) (eliminar x (cdr lista))))
     )
    )
  )
(write "Ejercicio 2 e")
(newline)
(eliminar 5 (list  9 8 7 6 5 4 3 2 1))
(eliminar 1 (list  9 8 7 6 5 4 3 2 1))
(eliminar 9 (list  9 8 7 6 5 4 3 2 1))

;Ejercicio 3 e

(define (imprime-complejo c)
  (newline)
  (write (parte-real c) )
  (write-char #\ )
  (write-char #\+ )
  (write-char #\ )
  (write (parte-compleja c))
  (write-char #\i )
  (newline)
  )

;Ejercicio 3 a

(define (complejo a b )
  (cons a b))

(define (parte-real c)
  (car c))

(define (parte-compleja c)
  (cdr c))


(define (suma-complejo c1 c2)
  (complejo (+ (parte-real c1)  (parte-real c2))
             (+(parte-compleja c1) (parte-compleja c2))
             )
  )
(write "Ejercicio 3 a")
(newline)
(imprime-complejo (suma-complejo (complejo 6 10) (complejo 4 12)))
(imprime-complejo (suma-complejo (complejo 1 0) (complejo -6 12)))
(imprime-complejo (suma-complejo (complejo 8 5) (complejo -6 -12)))


;Ejercicio 3 b

(define (resta-complejo c1 c2)
  (complejo (- (parte-real c1)  (parte-real c2))
             (- (parte-compleja c1) (parte-compleja c2))
             )
  )
(write "Ejercicio 3 b")
(newline)
(imprime-complejo (resta-complejo (complejo 6 10) (complejo 4 12)))
(imprime-complejo (resta-complejo (complejo 1 0) (complejo -6 12)))
(imprime-complejo (resta-complejo (complejo 8 5) (complejo -6 -12)))

;Ejercicio 3 c

(define (multipli-complejo c1 c2)
  (complejo (- (*(parte-real c1)  (parte-real c2)) (*(parte-compleja c1) (parte-compleja c2)))
               (+ (*(parte-real c1) (parte-compleja c2) (*(parte-compleja c1) (parte-real c2) )))
               )
  )
(write "Ejercicio 3 c")
(newline)
(imprime-complejo (multipli-complejo (complejo 6 5) (complejo 4 12)))
(imprime-complejo (multipli-complejo (complejo 1 0) (complejo -6 7)))
(imprime-complejo (multipli-complejo (complejo 8 5) (complejo -6 -12)))
            
;Ejercicio 3 d
(define (conjugado c)
  (complejo (parte-real c ) (* -1 (parte-compleja c))
   )
  )

(write "Ejercicio 3 d")
(newline)
(imprime-complejo (conjugado (complejo 4 12)))
(imprime-complejo (conjugado (complejo -6 7)))
(imprime-complejo (conjugado (complejo -6 -12)))



;Ejercicio 4

(define (divisibles lista x)
  (cond
    [(null? lista) '()]
    [( = (remainder (car lista) x) )  (list (list (car lista) (divisibles (cdr lista) x)) (list '()))]
    [(not( = (remainder (car lista) x))) (list (list '() ) (list(car lista ) (divisibles (cdr lista) x) )) ]
    )
  )
(write "Ejercicio 4")
(newline)
(divisibles '( 2 3 4 5 6 7 8 9) 2)







  
;Ejercicio 5
(define (pertenece? x lista)
  (if (null? lista)
      #f
      (if(= x (car lista))
         #t
         (pertenece? x (cdr lista))
         )
      )
  )


(define (resta lista1 lista2)
  (cond ((null? lista1) '())
        ((pertenece? (car lista1) lista2) (resta (cdr lista1) lista2))
        (#t (cons (car lista1) (resta (cdr lista1) lista2)))
        )
  )

(write "Ejercicio 5")
(newline)


(resta '(7 1 4 3 2 4 2 4 6) '(5 1 4))
(resta '(7 1 4 3 2 4 2 4 6) '(1 7 3 2))
(resta '(7 1 4 3 2 4 2 4 6) '(5 5 5 5))

;Ejercicio 6

(define (longitud L)
(if (null? L)
    0
    (+ 1 (longitud (cdr L)))))


(define (crea-pares lista1 lista2)
  (cond
    [(>= 0 (longitud lista1)) '()]
    [(>= 0 (longitud lista2)) '()]
    [ (= (longitud lista1) (longitud lista2)) (cons (car lista1) (cons (car lista2) (crea-pares (cdr lista1) (cdr lista2))))]
    [else '()]
    )
  )

(write "Ejercicio 6")
(newline)
(crea-pares '(9 8 ) '(1 2 ))
(crea-pares '(9 8 7 6 5 ) '(1 2 3))

(crea-pares '(9 8 7 6 5 ) '(1 2 3 4 5))
;Ejercicio 7

(define (es-factor? n k)
  ( = (remainder n k) 0)
  )

(define (factores n k)
  (cond
    [(> k n) '()]
    [(es-factor? n k) (cons k (factores (/ n k) k)) ]
    [else  (factores n (+ k 1)) ]
    )

  )
(write "Ejercicio 7")
(newline)
(factores 60 2)
(factores 36 2)
(factores 88 2)

;Ejercicio 8
(write "Ejercicio 8")
(newline)

(define (es-menor? k n)
  (< k n)
 )


(define (vuelto v lista)
  (cond
    [(null? lista) '()]
    [(= v (car lista))  (cons (car lista) '())]
    [(es-menor? v (car lista)) (vuelto v (cdr lista))]
    [else (cons (car lista) (vuelto (- v (car lista)) (cdr lista)))]
    )
  )

(define (resultado-vuelto)
  (define list-monedas (list 500 100 50 25 10 5 1))
  (write "Inserte el vuelto")
  (newline)
  (vuelto (read) list-monedas)
  
  )

(resultado-vuelto)

