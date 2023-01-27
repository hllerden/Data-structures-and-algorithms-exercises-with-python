## SQL ODEV 12

1-  film tablosunda film uzunluğu length sütununda gösterilmektedir. Uzunluğu ortalama film uzunluğundan fazla kaç tane film vardır?

    SELECT  COUNT(*) FROM film
    WHERE length> (
    SELECT AVG(length) FROM film)

2-  film tablosunda en yüksek rental_rate değerine sahip kaç tane film vardır?

    SELECT COUNT(*) FROM film
    WHERE rental_rate = (SELECT MAX(DISTINCT(rental_rate)) FROM film)

3-  film tablosunda en düşük rental_rate ve en düşün replacement_cost değerlerine sahip filmleri sıralayınız.

    SELECT * FROM film
    WHERE (rental_rate = (SELECT MIN(DISTINCT(rental_rate)) FROM film)) AND 
    (replacement_cost = (SELECT MIN(DISTINCT(replacement_cost)) FROM film))

4-  payment tablosunda en fazla sayıda alışveriş yapan müşterileri(customer) sıralayınız.

    SELECT customer.first_name, customer.last_name,payment.customer_id ,COUNT(payment.customer_id),SUM(payment.amount) FROM payment
    FULL JOIN  customer 
    ON customer.customer_id = payment.customer_id
    GROUP BY customer.first_name,customer.last_name,payment.customer_id
    ORDER BY COUNT(*) DESC