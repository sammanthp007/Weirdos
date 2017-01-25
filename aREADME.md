Done by: Samman Bikram Thapa @02755909 Howard University
You can access the code for the project at https://github.com/sammanthp007/CSCI350-functional-programming-assignment




A screenshot of the Github web page that shows the summary commit history of your project. 
 overall-commit-history.jpg 



*Screenshot taken using ImageMagick (www.imagemagick.org)


























The details of each commit, which can be obtained from Github web site. 


For problem 1:
Commit 1:     implement number 1 with flawed solution
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 12:01:27 2017 -0500
Difference: 


	

	

	

	

	+(define (nmember atm lis)
	

	

	+  (cond
	

	

	+    ((NULL? lis) #F) ;; empty list
	

	

	+    ((EQ? atm (CAR lis)) #T)
	

	

	+    (ELSE (nmember atm (CDR lis)))
	

	

	+    )
	

	

	+  )
	

	

	

	

	

	+;;; 1. (25 pts) Write a function (reverse-general L). L is a list. The result
	

	

	+;;; of the function is the reversed version of L. Every single sub-list in L
	

	

	+;;; should be reversed as well. For example, the result of
	

	

	+;;; (reverse-general ‘(a b (c (d e)) f) should be (f ((e d) c) b a).
	

	

	+
	

	

	+(define (reverse-general L)
	

	

	+  (cond
	

	

	+    ((NULL? L) '())
	

	

	+    (else (CONS (reverse-general (CDR L)) (CAR L)))
	

	

	+    )
	

	

	+  )
	

Commit 2: implement number 1: used append instead of cons
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 12:28:52 2017 -0500
Difference:




	

	;;; should be reversed as well. For example, the result of
	

	

	;;; (reverse-general ‘(a b (c (d e)) f) should be (f ((e d) c) b a).
	

	

	-
	

	

	(define (reverse-general L)
	

	

	  (cond
	

	

	    ((NULL? L) '())
	

	

	-    (else (CONS (reverse-general (CDR L)) (CAR L)))
	

	

	+    (else (append (reverse-general (CDR L)) (List (car L))))
	

	

	    )
	

	

	  )
	







































Commit 3: reverse-general: semi complete, used begin to make use of display while debugging
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 13:35:19 2017 -0500
Difference:


-    (else (append (reverse-general (CDR L)) (List (car L))))
	

	

	

	

	+    (else (append (reverse-general (CDR L)) ((lambda(x)
	

	

	+                                               (if (not (LIST? x))
	

	

	+                                                 (begin
	

	

	+                                                   (Display "h ") ;; displays when first char is not a list
	

	

	+                                                   (LIST x)) ;; return
	

	

	+                                                 (reverse-general x)
	

	

	+                                                 )
	

	

	+                                               ) (CAR L))
	

	

	+                  ))
	

	

	    )
	

	

	  )
	

	

	+
	

	

	+(reverse-general '(a b c))
	

	

	+(reverse-general '(a b ()))
	

	

	+(reverse-general '((a b c)))
	

	

	+
	

	

	+
	

	

	+
	



Commit 4: implement num one with debugging statements
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 16:20:07 2017 -0500
Difference: (Only the changed lines shown here)


-(define (nmember atm lis)
	

	

	

	

	-  (cond
	

	

	-    ((NULL? lis) #F) ;; empty list
	

	

	-    ((EQ? atm (CAR lis)) #T)
	

	

	-    (ELSE (nmember atm (CDR lis)))
	

	

	-    )
	

	

	-  )
	

	

	-                                               (if (not (LIST? x))
	

	

	+                                               (if (LIST? x)
	

	

	-                                                   (Display "h ") ;; displays when first char is not a list
	

	

	-                                                   (LIST x)) ;; return
	

	

	-                                                 (reverse-general x)
	

	

	+                                                   (Display "hello world") ;; displays
	

	

	+                                                   (LIST (reverse-general x)));; return
	

	

	+                                                 (list x)
	

	

	+(reverse-general '((a b c) (d e f)))
	

	

	+(reverse-general '(a (b c) ((d e) f) g))
	

	

	+(reverse-general '(1 (2 3) (4 (a (b (c d))))))
	

	

	+
	

	

	+
	

	

	+(reverse-general '(a b c))
	

	

	+(reverse-general '(a b ()))
	

	

	+(reverse-general '((a b c)))
	Commit 5: implement number 1 complete
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 16:21:45 2017 -0500
Difference:


-                                                 (begin
	

	

	

	

	-                                                   (Display "hello world") ;; displays
	

	

	-                                                   (LIST (reverse-general x)));; return
	

	

	+                                                 (LIST (reverse-general x));; return
	

	

	                                                 (list x)
	

	

	                                                 )
	

	

	                                               ) (CAR L))
	

	

	                  ))
	

	

	    )
	

	

	  )
	

	

	-(reverse-general '(a b c))
	

	

	-(reverse-general '(a b ()))
	

	

	-(reverse-general '((a b c)))
	

	

	-(reverse-general '((a b c) (d e f)))
	

	

	-(reverse-general '(a (b c) ((d e) f) g))
	

	

	-(reverse-general '(1 (2 3) (4 (a (b (c d))))))
	

	

	-
	

	

	-
	

	

	-(reverse-general '(a b c))
	

	

	-(reverse-general '(a b ()))
	

	

	-(reverse-general '((a b c)))
	







For Problem 2:
Commit 1: implement number 2: write the question for number 2 as comment
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 16:27:09 2017 -0500
Difference:


-                                                 (LIST (reverse-general x));; return
	

	

	

	

	+                                                 (LIST (reverse-general x))
	

	

	

	

	

	+;;; (25 pts) Write a function (sum-up-numbers-simple L). L is a list, which
	

	

	+;;; may contain as elements numbers and non-numbers. The result of the function
	

	

	+;;; is the sum of the numbers not in nested lists in L. If there are no such
	

	

	+;;; numbers, the result is zero. For example, the result of
	

	

	+;;; (sum-up-numbers-simple ‘(a b 1 2 c 3 d)) should be 6.
	



































Commit 2: implement number 2: write the logic for the solution in scheme
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:08:06 2017 -0500
Difference:
-;;; (25 pts) Write a function (sum-up-numbers-simple L). L is a list, which
	

	

	

	

	+;;; (25 pts) Write a function (sum-up-numbers-simple L). L is a list, which
	

	

	;;; may contain as elements numbers and non-numbers. The result of the function
	

	

	-;;; is the sum of the numbers not in nested lists in L. If there are no such
	

	

	-;;; numbers, the result is zero. For example, the result of
	

	

	+;;; is the sum of the numbers not in nested lists in L. If there are no such
	

	

	+;;; numbers, the result is zero. For example, the result of
	

	

	;;; (sum-up-numbers-simple ‘(a b 1 2 c 3 d)) should be 6.
	

	

	+(define (sum-up-numbers-simple L)
	

	

	+  (cond
	

	

	+    ; if L is empty list
	

	

	+    ((null? L) '0)
	

	

	+    ; if first element is list
	

	

	+    ((list? (car L)) (sum-up-numbers-simple(cdr L)))
	

	

	+    ; if first element is not a number
	

	

	+    ((not (number? (car L))) (sum-up-numbers-simple(cdr L)))
	

	

	+    ; calculate recursively
	

	

	+    (else (+ (car L) (sum-up-numbers-simple(cdr L)))
	

	

	+          ))
	

	

	+  )
	

Commit 3: implement 2: write test cases
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:11:46 2017 -0500
Difference:
+
	

	

	

	

	+(sum-up-numbers-simple '())
	

	

	+(sum-up-numbers-simple '(100 200))
	

	

	+(sum-up-numbers-simple '(a b c) )
	

	

	+(sum-up-numbers-simple '(100 a))
	

	

	+(sum-up-numbers-simple '(a 100))
	

	

	+(sum-up-numbers-simple '(a 100 b 200 c 300 d))
	

	

	+(sum-up-numbers-simple '(()))
	

	

	+(sum-up-numbers-simple '((100)))
	

	

	+(sum-up-numbers-simple '(100 (200)))
	

	

	+(sum-up-numbers-simple '(a 100 b (200) c 300 d))
	

	

	+
	

	

	+
	

	

	+
	

	

	+
	































Commit 4: implement number 2: comment out test cases
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:15:21 2017 -0500
Difference:


-(sum-up-numbers-simple '())
	

	

	

	

	-(sum-up-numbers-simple '(100 200))
	

	

	-(sum-up-numbers-simple '(a b c) )
	

	

	-(sum-up-numbers-simple '(100 a))
	

	

	-(sum-up-numbers-simple '(a 100))
	

	

	-(sum-up-numbers-simple '(a 100 b 200 c 300 d))
	

	

	-(sum-up-numbers-simple '(()))
	

	

	-(sum-up-numbers-simple '((100)))
	

	

	-(sum-up-numbers-simple '(100 (200)))
	

	

	-(sum-up-numbers-simple '(a 100 b (200) c 300 d))
	

	

	-
	

	

	+; (sum-up-numbers-simple '())
	

	

	+; (sum-up-numbers-simple '(100 200))
	

	

	+; (sum-up-numbers-simple '(a b c) )
	

	

	+; (sum-up-numbers-simple '(100 a))
	

	

	+; (sum-up-numbers-simple '(a 100))
	

	

	+; (sum-up-numbers-simple '(a 100 b 200 c 300 d))
	

	

	+; (sum-up-numbers-simple '(()))
	

	

	+; (sum-up-numbers-simple '((100)))
	

	

	+; (sum-up-numbers-simple '(100 (200)))
	

	

	+; (sum-up-numbers-simple '(a 100 b (200) c 300 d))
	

	

	+;
	











Commit 5:  implement number 2: add two new test cases, checked, and commented after they passed the expected results
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:19:00 2017 -0500
Difference:


-
	

	

	

	

	+; (sum-up-numbers-simple '(100 (200) (a) a b a c 200 (2)))
	

	

	+; (sum-up-numbers-simple '((((3)))))
	

	

	

	

For problem 3:
Commit 1:  implement number 3: write question
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:23:08 2017 -0500  
Difference:


+;;; (25 pts) Write a function (sum-up-numbers-general L). L is a list, which
	

	

	

	

	+;;; may contain as elements numbers and non-numbers. The result of the function
	

	

	+;;; is the sum of all the numbers (including those in nested lists) in L. If
	

	

	+;;; there are no such numbers, the result is zero. For example, the result of
	

	

	+;;; (sum-up-numbers-general ‘(a b 1 (2 c (3)) d)) should be 6.
	

	

	+
	



















Commit 2: implement number 3: copy the code of number 2 and change the name
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:50:29 2017 -0500
Difference:


+;(reverse-general '(a b c (d e f) g h))
	

	

	

	

	

	

	

	

	

	

	;;; (25 pts) Write a function (sum-up-numbers-simple L). L is a list, which
	

	@@ -61,4 +62,15 @@
	

	

	;;; there are no such numbers, the result is zero. For example, the result of
	

	

	;;; (sum-up-numbers-general ‘(a b 1 (2 c (3)) d)) should be 6.
	

	

	

	

	

	-
	

	

	+(define (sum-up-numbers-general L)
	

	

	+  (cond
	

	

	+    ; if L is empty list
	

	

	+    ((null? L) '0)
	

	

	+    ; if first element is list
	

	

	+    ((list? (car L)) (sum-up-numbers-general(cdr L)))
	

	

	+    ; if first element is not a number
	

	

	+    ((not (number? (car L))) (sum-up-numbers-general(cdr L)))
	

	

	+    ; calculate recursively
	

	

	+    (else (+ (car L) (sum-up-numbers-general(cdr L)))
	

	

	+          ))
	

	

	+  )
	







Commit 3: implement number 3: change the code to fit the requirement and test with custom test cases
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:52:29 2017 -0500
Difference: (only changed lines shown)


-    ((list? (car L)) (sum-up-numbers-general(cdr L)))
	

	

	

	

	+    ((list? (car L)) (+ (sum-up-numbers-general (car L)) (sum-up-numbers-general(cdr L))))
	

	

	+
	

	

	+(sum-up-numbers-general '(100 (200) (a) a b a c 200 (2)))
	

	

	+(sum-up-numbers-general '((((3)))))
	



Commit 4: test and validate the logic of the porgram with the given tests
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:55:21 2017 -0500
Difference:


-(sum-up-numbers-general '(100 (200) (a) a b a c 200 (2)))
	

	

	

	

	-(sum-up-numbers-general '((((3)))))
	

	

	+(sum-up-numbers-general '() )
	

	

	+(sum-up-numbers-general '(100) )
	

	

	+(sum-up-numbers-general '(100 200)  )
	

	

	+(sum-up-numbers-general '(a) )
	

	

	+(sum-up-numbers-general '(a 100 b 200 c 300 d) )
	

	

	+(sum-up-numbers-general '(()))
	

	

	+(sum-up-numbers-general '((100)))
	

	

	+(sum-up-numbers-general '(100 (200)))
	

	

	+(sum-up-numbers-general '(a 100 b (200) c 300 d))
	

	

	+(sum-up-numbers-general '(a 100 ((b ((200) c)) 300 d)))
	Commit 5:   implement number 3: comment out the test cases
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:56:37 2017 -0500
Difference:


-(sum-up-numbers-general '() )
	

	

	

	

	-(sum-up-numbers-general '(100) )
	

	

	-(sum-up-numbers-general '(100 200)  )
	

	

	-(sum-up-numbers-general '(a) )
	

	

	-(sum-up-numbers-general '(a 100 b 200 c 300 d) )
	

	

	-(sum-up-numbers-general '(()))
	

	

	-(sum-up-numbers-general '((100)))
	

	

	-(sum-up-numbers-general '(100 (200)))
	

	

	-(sum-up-numbers-general '(a 100 b (200) c 300 d))
	

	

	-(sum-up-numbers-general '(a 100 ((b ((200) c)) 300 d)))
	

	

	+;(sum-up-numbers-general '() )
	

	

	+;(sum-up-numbers-general '(100) )
	

	

	+;(sum-up-numbers-general '(100 200)  )
	

	

	+;(sum-up-numbers-general '(a) )
	

	

	+;(sum-up-numbers-general '(a 100 b 200 c 300 d) )
	

	

	+;(sum-up-numbers-general '(()))
	

	

	+;(sum-up-numbers-general '((100)))
	

	

	+;(sum-up-numbers-general '(100 (200)))
	

	

	+;(sum-up-numbers-general '(a 100 b (200) c 300 d))
	

	

	+;(sum-up-numbers-general '(a 100 ((b ((200) c)) 300 d)))
	













For problem 4:
Commit 1: implement 4: copy and paste the question number 4, will start working on it from tomorrow
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Mon Jan 23 22:59:36 2017 -0500
Difference:


+
	

	

	

	

	+;;; 4. (25 pts) Write a function (min-above-min L1 L2). L1 and L2 are both
	

	

	+;;; simple lists, which do not contain nested lists. Both lists may have
	

	

	+;;; non-numeric elements. The result of the function is the minimum of the
	

	

	+;;; numbers in L1 that are larger than the smallest number in L2. If there is
	

	

	+;;; no number in L2, all the numbers in L1 should be used to calculate the
	

	

	+;;; minimum. If there is no number in L1 larger than the smallest number in L2,
	

	

	+;;; the result is false (#F). For example, the result of
	

	

	+;;; (min-above-min ‘(2 a 1 3) ‘(b 5 3 1)) should be 2.
	

	

	+
	

	

	+
	





























Commit 2:  implement 3: implement min_atm_of function
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Tue Jan 24 14:18:26 2017 -0500
Difference:
+(define (min-above-min L1 L2)
	

	

	

	

	+  (cond
	

	

	+    ((null? l2) min_of (L1))
	

	

	+    (else (cond
	

	

	+            ((null? min_of ( greater_than (L1 (min_of L2)))) #f)
	

	

	+            (else (min_of ( greater_than (L1 (min_of L2)))))
	

	

	+            )
	

	

	+     )
	

	

	+  )
	

	

	+)
	

	

	+
	

	

	+
	

	

	+
	

	

	+
	

	

	+
	

	

	+
	

	

	+;;; returns the minimum number as an atom of the list
	

	

	+(define (min_atm_of lis)
	

	

	+  ; if the first atm is a number then
	

	

	+  (cond
	

	

	+    ((null? (cdr lis)) (car lis))
	

	

	+    ((not (number? (car lis))) (min_atm_of(cdr lis)))
	

	

	+    ((< (car lis) (min_atm_of(cdr lis))) (car lis))
	

	

	+    ; else return min from the remaining list
	

	

	+    (else (min_atm_of(cdr lis)))
	

	

	+  )
	

	

	+)
	

	

	

	

	

	+(min_atm_of '(10 12 3 4 22 4)) 
	Commit 3: implement number 4: implement greater_than helper function
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Tue Jan 24 14:39:51 2017 -0500
Difference: (Only changed lines shown here)


-    ((null? (cdr lis)) (cons (car lis) output))
	

	

	

	

	+    ((null? (cdr lis)) (if (> (car lis) val)
	

	

	+                           (cons (car lis) output)
	

	

	+                           output))
	

	

	+(greater_than '(1 3 5 2 6 4) '10 '())
	

	

	+
	

	

	-(min_atm_of '(10 12 3 4 22 4)) 
	

	

	+;(min_atm_of '(10 12 3 4 22 4)) 
	



Commit 4: implement 4: debug greater_than helper function from not working as expected when val > any item in the list
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Tue Jan 24 14:50:53 2017 -0500
Difference: (Only changed lines shown here)


-    ((null? (cdr lis)) (cons (car lis) output))
	

	

	

	

	+    ((null? (cdr lis)) (if (> (car lis) val)
	

	

	+                           (cons (car lis) output)
	

	

	+                           output))
	

	

	+(greater_than '(1 3 5 2 6 4) '10 '())
	

	

	+
	

	

	-(min_atm_of '(10 12 3 4 22 4)) 
	

	

	+;(min_atm_of '(10 12 3 4 22 4)) 
	









Commit 5:  implement number 4: testing and debugging - passed all given tests
Author: sammanthp007 <samman.thapa@bison.howard.edu>
Date:   Tue Jan 24 22:25:11 2017 -0500
Difference: (Only changed lines are shown)


-    ((null? (cdr lis)) (if (> (car lis) val)
	

	

	

	

	+    ((null? (cdr lis)) (if (and (number? (car lis)) (> (car lis) val))
	

	

	-    ((> (car lis) val) (greater_than (cdr lis) val (cons (car lis) output)))
	

	

	+    ((and (number? (car lis)) (> (car lis) val)) (greater_than (cdr lis) val (cons (car lis) output)))
	

	

	-    ((null? (cdr lis)) (car lis))
	

	

	+    ; if lis is empty return empty
	

	

	+    ((null? lis) #f)
	

	

	+    ; if (car lis) is not a number return min_atm_of(cdr lis)
	

	

	+    ; if (car lis) is a number and if (min_atm_of_cdr lis) is empty list
	

	

	+    ((and (number? (car lis)) (not (min_atm_of(cdr lis)))) (car lis))
	

	

	+    ; if (car lis) is a number and car lis is less than everything else
	

	

	-    ((null? l2) min_of (L1))
	

	

	+    ; If there is no number in L2, all the numbers in L1 should be used to calculate the minimum
	

	

	+    ((null? L2) (min_atm_of L1))
	

	

	+    ((null? L1) #f)
	

	

	+            ; if
	

	

	-(min-above-min '(2 4 3 5 6 4) '(4 5 6)) 
	

	

	+(min-above-min '() '(a 100 b 200 c 300 d))
	

	

	+(min-above-min '(100) '())
	

	

	+(min-above-min '(a 200 b 100 c 300 d)  '())
	

	

	+(min-above-min '(a) '())
	

	

	+(min-above-min '(a) '(a 200 b 300 c 100 d))
	

	

	+(min-above-min '(a b c) '(a 200 b 300 c 100 d))
	

	

	+(min-above-min '(a 200) '(a 200 b 300 c 100 d))
	

	

	+(min-above-min '(a 100) '(a 200 b 300 c 100 d))
	

	

	+(min-above-min '(100 200 300) '(300 100 200))
	

	

	+(min-above-min '(a 300 b 100 c 200 d) '(a 200 b 300 c 100 d))