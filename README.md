# price_collector
Collects prices of specific shopping mall items and notifies users when the price of the item is reduced

# create vapid use OpenSSL

- execute command for root
openssl ecparam -name prime256v1 -genkey -noout -out vapid_private.pem
openssl ec -in vapid_private.pem -pubout -out vapid_public.pem