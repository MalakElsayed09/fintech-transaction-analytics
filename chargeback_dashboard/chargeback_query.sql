SELECT
  merchant_id,
  (chargebacks * 1.0 / transactions) AS chargeback_rate
FROM chargebacks
WHERE (chargebacks * 1.0 / transactions) > 0.01;
