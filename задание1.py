SELECT c.login,
       COUNT(*) AS number_of_orders FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id=o."courierId"
WHERE o."inDelivery"=TRUE
GROUP BY c.login;