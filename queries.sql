-- Queries!

-- INSERT create new entries! 
INSERT INTO users ( email, name )
VALUES ("test@test.com", "Testman");

INSERT INTO addresses 
( street_name, state, zip, user_id)
VALUES
("123 fake", "OR", 97067, 2);

INSERT INTO pizzas_with_toppings
(pizza_id, topping_id)
VALUES
(1,1),
(1,2);


-- SELECT   SELECT what_we_want_to_display FROM where_we_want_to_get_it_from WHERE condition 
SELECT * FROM users ORDER BY id DESC limit 1 offset 1;

-- ORDER BY column  (ASC DESC)
-- LIMIT / OFFSET 
-- UPDATE
UPDATE users SET name = "Updateman", email = "email@email.man";
-- DELETE
SET SQL_SAFE_UPDATES = 0;

DELETE FROM users; -- don't do like this, add a where! 


SELECT *, length(name) AS whatsthis FROM users;