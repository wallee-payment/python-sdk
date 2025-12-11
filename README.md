# Wallee Python SDK

- API version: 2.0

The Wallee Python SDK is used to interact with Wallee's REST API.

## Requirements

Python 3.9 or later.

## Installation

### pip3 install (recommended)
```sh
pip3 install --upgrade wallee
```

### pip3 install from source via GitHub

```sh
pip3 install git+http://github.com/wallee-payment/python-sdk.git
```
(you may need to run `pip3` with root permission: `sudo pip3 install git+http://github.com/wallee-payment/python-sdk.git` )

### install from source via Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
pip3 install setuptools

python setup.py install
```

(or `sudo python setup.py install` to install the package for all users)

## Getting Started

Please follow the [installation](#installation) instructions, then run the following example:

```python
import wallee
from wallee.service.transactions_service import TransactionsService
from wallee.configuration import Configuration

application_user_id = 512
authentication_key = 'FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ='

configuration = Configuration(
    user_id=application_user_id,
    authentication_key=authentication_key
)

transactionsService = TransactionsService(configuration)

space_id = 405
transaction_id = 367155626
expand_set = ['group']

try:
    transaction = transactionsService.get_payment_transactions_id(
        transaction_id,
        space_id,
        expand_set
    )
    print("Transaction:")
    print(transaction)
except Exception as e:
    print("Exception when calling api: %s\n" % e)
```

## Documentation for API Endpoints
Additional Api services documentation: [*link*](https://app-wallee.com/en-us/doc/api/web-service#_services)<br>
Web Api client: [*link*](https://app-wallee.com//api/client)<br>
<details>
  <summary>Click here to see full list of services</summary>
  <br>All URIs are relative to https://app-wallee.com/<br>

  <p><strong>API Services:</strong></p>

- <strong>AccountsService</strong><br>
  &nbsp;&nbsp;* <code>delete_accounts_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /accounts/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete an account
  <br><br>
- <strong>AccountsService</strong><br>
  &nbsp;&nbsp;* <code>get_accounts</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /accounts
  &nbsp;&nbsp;&nbsp;&nbsp;List all accounts
  <br><br>
- <strong>AccountsService</strong><br>
  &nbsp;&nbsp;* <code>get_accounts_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /accounts/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve an account
  <br><br>
- <strong>AccountsService</strong><br>
  &nbsp;&nbsp;* <code>get_accounts_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /accounts/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search accounts
  <br><br>
- <strong>AccountsService</strong><br>
  &nbsp;&nbsp;* <code>patch_accounts_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /accounts/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update an account
  <br><br>
- <strong>AccountsService</strong><br>
  &nbsp;&nbsp;* <code>post_accounts</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /accounts
  &nbsp;&nbsp;&nbsp;&nbsp;Create an account
  <br><br>
- <strong>AccountsService</strong><br>
  &nbsp;&nbsp;* <code>post_accounts_id_activate</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /accounts/{id}/activate
  &nbsp;&nbsp;&nbsp;&nbsp;Activate an account
  <br><br>
- <strong>AccountsService</strong><br>
  &nbsp;&nbsp;* <code>post_accounts_id_deactivate</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /accounts/{id}/deactivate
  &nbsp;&nbsp;&nbsp;&nbsp;Deactivate an account
  <br><br>
- <strong>AnalyticsQueriesService</strong><br>
  &nbsp;&nbsp;* <code>delete_analytics_queries_query_external_id_query_external_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /analytics/queries/queryExternalId/{queryExternalId}
  &nbsp;&nbsp;&nbsp;&nbsp;Cancel a query execution, identifying it by its external id.
  <br><br>
- <strong>AnalyticsQueriesService</strong><br>
  &nbsp;&nbsp;* <code>delete_analytics_queries_query_token_query_token</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /analytics/queries/queryToken/{queryToken}
  &nbsp;&nbsp;&nbsp;&nbsp;Cancel a query execution, identifying it by its query token.
  <br><br>
- <strong>AnalyticsQueriesService</strong><br>
  &nbsp;&nbsp;* <code>get_analytics_queries</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /analytics/queries
  &nbsp;&nbsp;&nbsp;&nbsp;Get portion of query executions for account
  <br><br>
- <strong>AnalyticsQueriesService</strong><br>
  &nbsp;&nbsp;* <code>get_analytics_queries_query_external_id_query_external_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /analytics/queries/queryExternalId/{queryExternalId}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a query execution information by its external id
  <br><br>
- <strong>AnalyticsQueriesService</strong><br>
  &nbsp;&nbsp;* <code>get_analytics_queries_query_external_id_query_external_id_result</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /analytics/queries/queryExternalId/{queryExternalId}/result
  &nbsp;&nbsp;&nbsp;&nbsp;Generate a temporary URL to download the query result. It retrieves the query by its external id
  <br><br>
- <strong>AnalyticsQueriesService</strong><br>
  &nbsp;&nbsp;* <code>get_analytics_queries_query_token_query_token</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /analytics/queries/queryToken/{queryToken}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a query execution information by its query token
  <br><br>
- <strong>AnalyticsQueriesService</strong><br>
  &nbsp;&nbsp;* <code>get_analytics_queries_query_token_query_token_result</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /analytics/queries/queryToken/{queryToken}/result
  &nbsp;&nbsp;&nbsp;&nbsp;Generate a temporary URL to download the query result. It retrieves the query by its query token
  <br><br>
- <strong>AnalyticsQueriesService</strong><br>
  &nbsp;&nbsp;* <code>post_analytics_queries_submit</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /analytics/queries/submit
  &nbsp;&nbsp;&nbsp;&nbsp;Submit a query execution
  <br><br>
- <strong>ApplicationUsersService</strong><br>
  &nbsp;&nbsp;* <code>delete_application_users_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /application-users/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete an application user
  <br><br>
- <strong>ApplicationUsersService</strong><br>
  &nbsp;&nbsp;* <code>delete_application_users_user_id_keys_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /application-users/{userId}/keys/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Deactivate an authentication key
  <br><br>
- <strong>ApplicationUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_application_users</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /application-users
  &nbsp;&nbsp;&nbsp;&nbsp;List all application users
  <br><br>
- <strong>ApplicationUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_application_users_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /application-users/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve an application user
  <br><br>
- <strong>ApplicationUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_application_users_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /application-users/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search application users
  <br><br>
- <strong>ApplicationUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_application_users_user_id_keys</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /application-users/{userId}/keys
  &nbsp;&nbsp;&nbsp;&nbsp;List a user&#39;s authentication keys
  <br><br>
- <strong>ApplicationUsersService</strong><br>
  &nbsp;&nbsp;* <code>patch_application_users_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /application-users/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update an application user
  <br><br>
- <strong>ApplicationUsersService</strong><br>
  &nbsp;&nbsp;* <code>post_application_users</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /application-users
  &nbsp;&nbsp;&nbsp;&nbsp;Create an application user
  <br><br>
- <strong>ApplicationUsersService</strong><br>
  &nbsp;&nbsp;* <code>post_application_users_user_id_keys</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /application-users/{userId}/keys
  &nbsp;&nbsp;&nbsp;&nbsp;Generate a new authentication key
  <br><br>
- <strong>ApplicationUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>delete_application_users_user_id_account_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /application-users/{userId}/account-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Unassign a role from an application user for an account
  <br><br>
- <strong>ApplicationUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>delete_application_users_user_id_space_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /application-users/{userId}/space-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Unassign a role from an application user for a space
  <br><br>
- <strong>ApplicationUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>get_application_users_user_id_account_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /application-users/{userId}/account-roles
  &nbsp;&nbsp;&nbsp;&nbsp;List all roles of an application user for an account
  <br><br>
- <strong>ApplicationUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>get_application_users_user_id_space_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /application-users/{userId}/space-roles
  &nbsp;&nbsp;&nbsp;&nbsp;List all roles of an application user for a space
  <br><br>
- <strong>ApplicationUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>post_application_users_user_id_account_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /application-users/{userId}/account-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Assign a role to an application user for an account
  <br><br>
- <strong>ApplicationUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>post_application_users_user_id_space_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /application-users/{userId}/space-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Assign a role to an application user for a space
  <br><br>
- <strong>BankAccountsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_accounts</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-accounts
  &nbsp;&nbsp;&nbsp;&nbsp;List all bank accounts
  <br><br>
- <strong>BankAccountsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_accounts_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-accounts/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a bank account
  <br><br>
- <strong>BankAccountsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_accounts_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-accounts/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search bank accounts
  <br><br>
- <strong>BankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions
  &nbsp;&nbsp;&nbsp;&nbsp;List all bank transactions
  <br><br>
- <strong>BankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a bank transaction
  <br><br>
- <strong>BankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search bank transactions
  <br><br>
- <strong>ChargeAttemptsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_attempts</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-attempts
  &nbsp;&nbsp;&nbsp;&nbsp;List all charge attempts
  <br><br>
- <strong>ChargeAttemptsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_attempts_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-attempts/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a charge attempt
  <br><br>
- <strong>ChargeAttemptsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_attempts_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-attempts/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search charge attempts
  <br><br>
- <strong>ChargeBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_charges</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/charges
  &nbsp;&nbsp;&nbsp;&nbsp;List all charge bank transactions
  <br><br>
- <strong>ChargeBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_charges_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/charges/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a charge bank transaction
  <br><br>
- <strong>ChargeBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_charges_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/charges/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search charge bank transactions
  <br><br>
- <strong>ChargeFlowLevelsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_flows_levels</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-flows/levels
  &nbsp;&nbsp;&nbsp;&nbsp;List all charge flow levels
  <br><br>
- <strong>ChargeFlowLevelsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_flows_levels_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-flows/levels/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a charge flow level
  <br><br>
- <strong>ChargeFlowLevelsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_flows_levels_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-flows/levels/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search charge flow levels
  <br><br>
- <strong>ChargeFlowLevelsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_charge_flows_levels_id_send_message</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/charge-flows/levels/{id}/send-message
  &nbsp;&nbsp;&nbsp;&nbsp;Send a payment link
  <br><br>
- <strong>ChargeFlowsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_flows</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-flows
  &nbsp;&nbsp;&nbsp;&nbsp;List all charge flows
  <br><br>
- <strong>ChargeFlowsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_flows_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-flows/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a charge flow
  <br><br>
- <strong>ChargeFlowsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_flows_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-flows/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search charge flows
  <br><br>
- <strong>ChargeFlowsLevelPaymentLinksService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_flows_levels_payment_links</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-flows/levels/payment-links
  &nbsp;&nbsp;&nbsp;&nbsp;List all charge flow payment links
  <br><br>
- <strong>ChargeFlowsLevelPaymentLinksService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_flows_levels_payment_links_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-flows/levels/payment-links/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a charge flow payment link
  <br><br>
- <strong>ChargeFlowsLevelPaymentLinksService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_charge_flows_levels_payment_links_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/charge-flows/levels/payment-links/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search charge flow payment links
  <br><br>
- <strong>ConditionTypesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_condition_types</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/condition-types
  &nbsp;&nbsp;&nbsp;&nbsp;List all condition types.
  <br><br>
- <strong>ConditionTypesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_condition_types_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/condition-types/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a condition type.
  <br><br>
- <strong>ConditionTypesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_condition_types_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/condition-types/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search condition types.
  <br><br>
- <strong>ConsumedResourcesService</strong><br>
  &nbsp;&nbsp;* <code>get_spaces_consumed_resources</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /spaces/consumed-resources
  &nbsp;&nbsp;&nbsp;&nbsp;List consumed resources
  <br><br>
- <strong>CountriesService</strong><br>
  &nbsp;&nbsp;* <code>get_countries</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /countries
  &nbsp;&nbsp;&nbsp;&nbsp;List all countries
  <br><br>
- <strong>CountriesService</strong><br>
  &nbsp;&nbsp;* <code>get_countries_code</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /countries/{code}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a country
  <br><br>
- <strong>CountriesService</strong><br>
  &nbsp;&nbsp;* <code>get_countries_country_code_states</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /countries/{countryCode}/states
  &nbsp;&nbsp;&nbsp;&nbsp;List all states for a country
  <br><br>
- <strong>CountriesService</strong><br>
  &nbsp;&nbsp;* <code>get_countries_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /countries/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search countries
  <br><br>
- <strong>CountriesService</strong><br>
  &nbsp;&nbsp;* <code>get_countries_states</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /countries/states
  &nbsp;&nbsp;&nbsp;&nbsp;List all country states
  <br><br>
- <strong>CountriesService</strong><br>
  &nbsp;&nbsp;* <code>get_countries_states_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /countries/states/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a country state
  <br><br>
- <strong>CurrenciesService</strong><br>
  &nbsp;&nbsp;* <code>get_currencies</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /currencies
  &nbsp;&nbsp;&nbsp;&nbsp;List all currencies
  <br><br>
- <strong>CurrenciesService</strong><br>
  &nbsp;&nbsp;* <code>get_currencies_code</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /currencies/{code}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a currency
  <br><br>
- <strong>CurrenciesService</strong><br>
  &nbsp;&nbsp;* <code>get_currencies_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /currencies/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search currencies
  <br><br>
- <strong>CurrencyBankAccountsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_currency_bank_accounts</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/currency-bank-accounts
  &nbsp;&nbsp;&nbsp;&nbsp;List all currency bank accounts
  <br><br>
- <strong>CurrencyBankAccountsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_currency_bank_accounts_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/currency-bank-accounts/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a currency bank account
  <br><br>
- <strong>CurrencyBankAccountsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_currency_bank_accounts_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/currency-bank-accounts/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search currency bank accounts
  <br><br>
- <strong>CustomerAddressesService</strong><br>
  &nbsp;&nbsp;* <code>delete_customers_customer_id_addresses_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /customers/{customerId}/addresses/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a customer address
  <br><br>
- <strong>CustomerAddressesService</strong><br>
  &nbsp;&nbsp;* <code>get_customers_customer_id_addresses</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers/{customerId}/addresses
  &nbsp;&nbsp;&nbsp;&nbsp;List all customer addresses
  <br><br>
- <strong>CustomerAddressesService</strong><br>
  &nbsp;&nbsp;* <code>get_customers_customer_id_addresses_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers/{customerId}/addresses/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a customer address
  <br><br>
- <strong>CustomerAddressesService</strong><br>
  &nbsp;&nbsp;* <code>get_customers_customer_id_addresses_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers/{customerId}/addresses/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search customer addresses
  <br><br>
- <strong>CustomerAddressesService</strong><br>
  &nbsp;&nbsp;* <code>patch_customers_customer_id_addresses_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /customers/{customerId}/addresses/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a customer address
  <br><br>
- <strong>CustomerAddressesService</strong><br>
  &nbsp;&nbsp;* <code>post_customers_customer_id_addresses</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /customers/{customerId}/addresses
  &nbsp;&nbsp;&nbsp;&nbsp;Create a customer address
  <br><br>
- <strong>CustomerAddressesService</strong><br>
  &nbsp;&nbsp;* <code>post_customers_customer_id_addresses_id_default</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /customers/{customerId}/addresses/{id}/default
  &nbsp;&nbsp;&nbsp;&nbsp;Set the default address for a customer
  <br><br>
- <strong>CustomerCommentsService</strong><br>
  &nbsp;&nbsp;* <code>delete_customers_customer_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /customers/{customerId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a customer comment
  <br><br>
- <strong>CustomerCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_customers_customer_id_comments</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers/{customerId}/comments
  &nbsp;&nbsp;&nbsp;&nbsp;List all customer comments
  <br><br>
- <strong>CustomerCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_customers_customer_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers/{customerId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a customer comment
  <br><br>
- <strong>CustomerCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_customers_customer_id_comments_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers/{customerId}/comments/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search customer comments
  <br><br>
- <strong>CustomerCommentsService</strong><br>
  &nbsp;&nbsp;* <code>patch_customers_customer_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /customers/{customerId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a customer comment
  <br><br>
- <strong>CustomerCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_customers_customer_id_comments</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /customers/{customerId}/comments
  &nbsp;&nbsp;&nbsp;&nbsp;Create a customer comment
  <br><br>
- <strong>CustomerCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_customers_customer_id_comments_id_pin</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /customers/{customerId}/comments/{id}/pin
  &nbsp;&nbsp;&nbsp;&nbsp;Pin a comment to the top
  <br><br>
- <strong>CustomerCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_customers_customer_id_comments_id_unpin</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /customers/{customerId}/comments/{id}/unpin
  &nbsp;&nbsp;&nbsp;&nbsp;Remove a pinned comment from the top
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>delete_customers_bulk</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /customers/bulk
  &nbsp;&nbsp;&nbsp;&nbsp;Delete multiple customers
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>delete_customers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /customers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a customer
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>get_customers</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers
  &nbsp;&nbsp;&nbsp;&nbsp;List all customers
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>get_customers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a customer
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>get_customers_id_email_addresses</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers/{id}/email-addresses
  &nbsp;&nbsp;&nbsp;&nbsp;List a customer&#39;s email addresses
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>get_customers_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /customers/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search customers
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>patch_customers_bulk</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /customers/bulk
  &nbsp;&nbsp;&nbsp;&nbsp;Update multiple customers
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>patch_customers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /customers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a customer
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>post_customers</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /customers
  &nbsp;&nbsp;&nbsp;&nbsp;Create a customer
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>post_customers_bulk</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /customers/bulk
  &nbsp;&nbsp;&nbsp;&nbsp;Create multiple customers
  <br><br>
- <strong>CustomersService</strong><br>
  &nbsp;&nbsp;* <code>post_customers_id_merge_other</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /customers/{id}/merge/{other}
  &nbsp;&nbsp;&nbsp;&nbsp;Merge two customers
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>delete_debt_collection_cases_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /debt-collection/cases/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a debt collection case
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_cases</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/cases
  &nbsp;&nbsp;&nbsp;&nbsp;List all debt collection cases
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_cases_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/cases/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a debt collection case
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_cases_id_documents</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/cases/{id}/documents
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve all documents of a debt collection case
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_cases_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/cases/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search debt collection cases
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>patch_debt_collection_cases_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /debt-collection/cases/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a debt collection case
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>post_debt_collection_cases</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /debt-collection/cases
  &nbsp;&nbsp;&nbsp;&nbsp;Create a debt collection case
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>post_debt_collection_cases_id_close</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /debt-collection/cases/{id}/close
  &nbsp;&nbsp;&nbsp;&nbsp;Close a debt collection case
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>post_debt_collection_cases_id_documents</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /debt-collection/cases/{id}/documents
  &nbsp;&nbsp;&nbsp;&nbsp;Attach a document to a debt collection case
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>post_debt_collection_cases_id_mark_prepared</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /debt-collection/cases/{id}/mark-prepared
  &nbsp;&nbsp;&nbsp;&nbsp;Mark a debt collection case as prepared
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>post_debt_collection_cases_id_mark_reviewed</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /debt-collection/cases/{id}/mark-reviewed
  &nbsp;&nbsp;&nbsp;&nbsp;Mark a debt collection case as reviewed
  <br><br>
- <strong>DebtCollectionCasesService</strong><br>
  &nbsp;&nbsp;* <code>post_debt_collection_cases_id_payment_receipts</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /debt-collection/cases/{id}/payment-receipts
  &nbsp;&nbsp;&nbsp;&nbsp;Create a payment receipt for a debt collection case
  <br><br>
- <strong>DebtCollectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>delete_debt_collection_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /debt-collection/configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a debt collector configuration
  <br><br>
- <strong>DebtCollectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/configurations
  &nbsp;&nbsp;&nbsp;&nbsp;List all debt collector configurations
  <br><br>
- <strong>DebtCollectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a debt collector configuration
  <br><br>
- <strong>DebtCollectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_configurations_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/configurations/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search debt collector configurations
  <br><br>
- <strong>DebtCollectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>patch_debt_collection_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /debt-collection/configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a debt collector configuration
  <br><br>
- <strong>DebtCollectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>post_debt_collection_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /debt-collection/configurations
  &nbsp;&nbsp;&nbsp;&nbsp;Create a debt collector configuration
  <br><br>
- <strong>DebtCollectorsService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_collectors</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/collectors
  &nbsp;&nbsp;&nbsp;&nbsp;List all debt collectors
  <br><br>
- <strong>DebtCollectorsService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_collectors_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/collectors/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a debt collector
  <br><br>
- <strong>DebtCollectorsService</strong><br>
  &nbsp;&nbsp;* <code>get_debt_collection_collectors_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /debt-collection/collectors/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search debt collectors
  <br><br>
- <strong>DeliveryIndicationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_delivery_indications</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/delivery-indications
  &nbsp;&nbsp;&nbsp;&nbsp;List all delivery indications
  <br><br>
- <strong>DeliveryIndicationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_delivery_indications_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/delivery-indications/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a delivery indication
  <br><br>
- <strong>DeliveryIndicationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_delivery_indications_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/delivery-indications/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search delivery indications
  <br><br>
- <strong>DeliveryIndicationsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_delivery_indications_id_mark_not_suitable</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/delivery-indications/{id}/mark-not-suitable
  &nbsp;&nbsp;&nbsp;&nbsp;Mark a delivery indication as not suitable.
  <br><br>
- <strong>DeliveryIndicationsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_delivery_indications_id_mark_suitable</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/delivery-indications/{id}/mark-suitable
  &nbsp;&nbsp;&nbsp;&nbsp;Mark a delivery indication as suitable.
  <br><br>
- <strong>DocumentTemplateTypesService</strong><br>
  &nbsp;&nbsp;* <code>get_document_templates_types</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /document-templates/types
  &nbsp;&nbsp;&nbsp;&nbsp;List all document template types
  <br><br>
- <strong>DocumentTemplateTypesService</strong><br>
  &nbsp;&nbsp;* <code>get_document_templates_types_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /document-templates/types/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a document template type
  <br><br>
- <strong>DocumentTemplateTypesService</strong><br>
  &nbsp;&nbsp;* <code>get_document_templates_types_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /document-templates/types/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search document template types
  <br><br>
- <strong>DocumentTemplatesService</strong><br>
  &nbsp;&nbsp;* <code>get_document_templates</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /document-templates
  &nbsp;&nbsp;&nbsp;&nbsp;List all document templates
  <br><br>
- <strong>DocumentTemplatesService</strong><br>
  &nbsp;&nbsp;* <code>get_document_templates_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /document-templates/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a document template
  <br><br>
- <strong>DocumentTemplatesService</strong><br>
  &nbsp;&nbsp;* <code>get_document_templates_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /document-templates/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search document templates
  <br><br>
- <strong>DunningCasesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_dunning_cases</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/dunning-cases
  &nbsp;&nbsp;&nbsp;&nbsp;List all dunning cases
  <br><br>
- <strong>DunningCasesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_dunning_cases_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/dunning-cases/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a dunning case
  <br><br>
- <strong>DunningCasesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_dunning_cases_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/dunning-cases/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search dunning cases
  <br><br>
- <strong>DunningCasesService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_dunning_cases_id_suspend</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/dunning-cases/{id}/suspend
  &nbsp;&nbsp;&nbsp;&nbsp;Suspend a dunning case
  <br><br>
- <strong>DunningCasesService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_dunning_cases_invoice_invoice_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/dunning-cases/invoice/{invoiceId}
  &nbsp;&nbsp;&nbsp;&nbsp;Create a dunning case for an invoice
  <br><br>
- <strong>DunningFlowLevelsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_dunning_flows_levels</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/dunning-flows/levels
  &nbsp;&nbsp;&nbsp;&nbsp;List all dunning flow levels
  <br><br>
- <strong>DunningFlowLevelsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_dunning_flows_levels_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/dunning-flows/levels/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a dunning flow level
  <br><br>
- <strong>DunningFlowLevelsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_dunning_flows_levels_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/dunning-flows/levels/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search dunning flow levels
  <br><br>
- <strong>DunningFlowsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_dunning_flows</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/dunning-flows
  &nbsp;&nbsp;&nbsp;&nbsp;List all dunning flows
  <br><br>
- <strong>DunningFlowsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_dunning_flows_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/dunning-flows/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a dunning flow
  <br><br>
- <strong>DunningFlowsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_dunning_flows_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/dunning-flows/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search dunning flows
  <br><br>
- <strong>ExpressCheckoutService</strong><br>
  &nbsp;&nbsp;* <code>post_express_checkout_create_session</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /express-checkout/create-session
  &nbsp;&nbsp;&nbsp;&nbsp;Create a new Express Checkout Session
  <br><br>
- <strong>ExternalTransferBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_external_transfers</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/external-transfers
  &nbsp;&nbsp;&nbsp;&nbsp;List all external transfer bank transactions
  <br><br>
- <strong>ExternalTransferBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_external_transfers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/external-transfers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve an external transfer bank transaction
  <br><br>
- <strong>ExternalTransferBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_external_transfers_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/external-transfers/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search external transfer bank transactions
  <br><br>
- <strong>HumanUsersService</strong><br>
  &nbsp;&nbsp;* <code>delete_human_users_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /human-users/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a human user
  <br><br>
- <strong>HumanUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_human_users</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /human-users
  &nbsp;&nbsp;&nbsp;&nbsp;List all human users
  <br><br>
- <strong>HumanUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_human_users_export</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /human-users/export
  &nbsp;&nbsp;&nbsp;&nbsp;Export human users
  <br><br>
- <strong>HumanUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_human_users_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /human-users/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a human user
  <br><br>
- <strong>HumanUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_human_users_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /human-users/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search human users
  <br><br>
- <strong>HumanUsersService</strong><br>
  &nbsp;&nbsp;* <code>patch_human_users_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /human-users/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a human user
  <br><br>
- <strong>HumanUsersService</strong><br>
  &nbsp;&nbsp;* <code>post_human_users</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /human-users
  &nbsp;&nbsp;&nbsp;&nbsp;Create a human user
  <br><br>
- <strong>HumanUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>delete_human_users_user_id_account_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /human-users/{userId}/account-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Unassign a role from a human user for an account
  <br><br>
- <strong>HumanUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>delete_human_users_user_id_space_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /human-users/{userId}/space-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Unassign a role from a human user for a space
  <br><br>
- <strong>HumanUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>get_human_users_user_id_account_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /human-users/{userId}/account-roles
  &nbsp;&nbsp;&nbsp;&nbsp;List all roles of a human user for an account
  <br><br>
- <strong>HumanUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>get_human_users_user_id_space_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /human-users/{userId}/space-roles
  &nbsp;&nbsp;&nbsp;&nbsp;List all roles of a human user for a space
  <br><br>
- <strong>HumanUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>post_human_users_user_id_account_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /human-users/{userId}/account-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Assign a role to a human user for an account
  <br><br>
- <strong>HumanUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>post_human_users_user_id_space_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /human-users/{userId}/space-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Assign a role to a human user for a space
  <br><br>
- <strong>InternalTransferBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_internal_transfers</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/internal-transfers
  &nbsp;&nbsp;&nbsp;&nbsp;List all internal transfer bank transactions
  <br><br>
- <strong>InternalTransferBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_internal_transfers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/internal-transfers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve an internal transfer bank transaction
  <br><br>
- <strong>InternalTransferBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_internal_transfers_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/internal-transfers/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search internal transfer bank transactions
  <br><br>
- <strong>LabelDescriptorsService</strong><br>
  &nbsp;&nbsp;* <code>get_label_descriptors</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /label-descriptors
  &nbsp;&nbsp;&nbsp;&nbsp;List all label descriptors
  <br><br>
- <strong>LabelDescriptorsService</strong><br>
  &nbsp;&nbsp;* <code>get_label_descriptors_groups</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /label-descriptors/groups
  &nbsp;&nbsp;&nbsp;&nbsp;List all label descriptor groups
  <br><br>
- <strong>LabelDescriptorsService</strong><br>
  &nbsp;&nbsp;* <code>get_label_descriptors_groups_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /label-descriptors/groups/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a label descriptor group
  <br><br>
- <strong>LabelDescriptorsService</strong><br>
  &nbsp;&nbsp;* <code>get_label_descriptors_groups_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /label-descriptors/groups/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search label descriptor groups
  <br><br>
- <strong>LabelDescriptorsService</strong><br>
  &nbsp;&nbsp;* <code>get_label_descriptors_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /label-descriptors/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a label descriptor
  <br><br>
- <strong>LabelDescriptorsService</strong><br>
  &nbsp;&nbsp;* <code>get_label_descriptors_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /label-descriptors/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search label descriptors
  <br><br>
- <strong>LanguagesService</strong><br>
  &nbsp;&nbsp;* <code>get_languages</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /languages
  &nbsp;&nbsp;&nbsp;&nbsp;List all languages
  <br><br>
- <strong>LanguagesService</strong><br>
  &nbsp;&nbsp;* <code>get_languages_code</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /languages/{code}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a language
  <br><br>
- <strong>LanguagesService</strong><br>
  &nbsp;&nbsp;* <code>get_languages_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /languages/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search languages
  <br><br>
- <strong>LegalOrganizationFormsService</strong><br>
  &nbsp;&nbsp;* <code>get_legal_organization_forms</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /legal-organization-forms
  &nbsp;&nbsp;&nbsp;&nbsp;List all legal organization forms
  <br><br>
- <strong>LegalOrganizationFormsService</strong><br>
  &nbsp;&nbsp;* <code>get_legal_organization_forms_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /legal-organization-forms/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a legal organization form
  <br><br>
- <strong>LegalOrganizationFormsService</strong><br>
  &nbsp;&nbsp;* <code>get_legal_organization_forms_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /legal-organization-forms/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search legal organization forms
  <br><br>
- <strong>ManualTasksService</strong><br>
  &nbsp;&nbsp;* <code>get_manual_tasks</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /manual-tasks
  &nbsp;&nbsp;&nbsp;&nbsp;List all manual tasks
  <br><br>
- <strong>ManualTasksService</strong><br>
  &nbsp;&nbsp;* <code>get_manual_tasks_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /manual-tasks/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a manual task
  <br><br>
- <strong>ManualTasksService</strong><br>
  &nbsp;&nbsp;* <code>get_manual_tasks_id_notification</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /manual-tasks/{id}/notification
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a manual task&#39;s notification message
  <br><br>
- <strong>ManualTasksService</strong><br>
  &nbsp;&nbsp;* <code>get_manual_tasks_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /manual-tasks/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search manual tasks
  <br><br>
- <strong>ManualTasksService</strong><br>
  &nbsp;&nbsp;* <code>post_manual_tasks_id_action_action_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /manual-tasks/{id}/action/{actionId}
  &nbsp;&nbsp;&nbsp;&nbsp;Process a manual task&#39;s action
  <br><br>
- <strong>PaymentConnectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_connector_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/connector-configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a payment connector configuration
  <br><br>
- <strong>PaymentConnectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_connector_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/connector-configurations
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment connector configurations
  <br><br>
- <strong>PaymentConnectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_connector_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/connector-configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment connector configuration
  <br><br>
- <strong>PaymentConnectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_connector_configurations_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/connector-configurations/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment connector configurations
  <br><br>
- <strong>PaymentConnectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_connector_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/connector-configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a payment connector configuration
  <br><br>
- <strong>PaymentConnectorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_connector_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/connector-configurations
  &nbsp;&nbsp;&nbsp;&nbsp;Create a payment connector configuration
  <br><br>
- <strong>PaymentConnectorsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_connectors</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/connectors
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment connectors.
  <br><br>
- <strong>PaymentConnectorsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_connectors_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/connectors/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment connector.
  <br><br>
- <strong>PaymentConnectorsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_connectors_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/connectors/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment connectors.
  <br><br>
- <strong>PaymentLinksService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_links_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/links/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a payment link
  <br><br>
- <strong>PaymentLinksService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_links</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/links
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment links
  <br><br>
- <strong>PaymentLinksService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_links_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/links/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment link
  <br><br>
- <strong>PaymentLinksService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_links_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/links/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment links
  <br><br>
- <strong>PaymentLinksService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_links_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/links/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a payment link
  <br><br>
- <strong>PaymentLinksService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_links</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/links
  &nbsp;&nbsp;&nbsp;&nbsp;Create a payment link
  <br><br>
- <strong>PaymentMethodBrandsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_method_brands</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/method-brands
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment method brands.
  <br><br>
- <strong>PaymentMethodBrandsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_method_brands_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/method-brands/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment method brand.
  <br><br>
- <strong>PaymentMethodBrandsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_method_brands_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/method-brands/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment method brands.
  <br><br>
- <strong>PaymentMethodConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_method_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/method-configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a payment method configuration
  <br><br>
- <strong>PaymentMethodConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_method_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/method-configurations
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment method configurations
  <br><br>
- <strong>PaymentMethodConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_method_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/method-configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment method configuration
  <br><br>
- <strong>PaymentMethodConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_method_configurations_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/method-configurations/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment method configurations
  <br><br>
- <strong>PaymentMethodConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_method_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/method-configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a payment method configuration
  <br><br>
- <strong>PaymentMethodConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_method_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/method-configurations
  &nbsp;&nbsp;&nbsp;&nbsp;Create a payment method configuration
  <br><br>
- <strong>PaymentMethodsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_methods</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/methods
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment methods.
  <br><br>
- <strong>PaymentMethodsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_methods_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/methods/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment method.
  <br><br>
- <strong>PaymentMethodsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_methods_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/methods/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment methods.
  <br><br>
- <strong>PaymentProcessorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_processor_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/processor-configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a payment processor configuration
  <br><br>
- <strong>PaymentProcessorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_processor_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/processor-configurations
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment processor configurations
  <br><br>
- <strong>PaymentProcessorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_processor_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/processor-configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment processor configuration
  <br><br>
- <strong>PaymentProcessorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_processor_configurations_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/processor-configurations/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment processor configurations
  <br><br>
- <strong>PaymentProcessorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_processor_configurations_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/processor-configurations/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a payment processor configuration
  <br><br>
- <strong>PaymentProcessorConfigurationsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_processor_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/processor-configurations
  &nbsp;&nbsp;&nbsp;&nbsp;Create a payment processor configuration
  <br><br>
- <strong>PaymentProcessorsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_processors</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/processors
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment processors.
  <br><br>
- <strong>PaymentProcessorsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_processors_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/processors/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment processor.
  <br><br>
- <strong>PaymentProcessorsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_processors_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/processors/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment processors.
  <br><br>
- <strong>PaymentSalesChannelsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_sales_channels</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/sales-channels
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment sales channels.
  <br><br>
- <strong>PaymentSalesChannelsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_sales_channels_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/sales-channels/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment sales channel.
  <br><br>
- <strong>PaymentSalesChannelsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_sales_channels_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/sales-channels/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment sales channels.
  <br><br>
- <strong>PaymentTerminalTransactionSummariesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_terminals_transaction_summaries</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/terminals/transaction-summaries
  &nbsp;&nbsp;&nbsp;&nbsp;List all summaries
  <br><br>
- <strong>PaymentTerminalTransactionSummariesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_terminals_transaction_summaries_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/terminals/transaction-summaries/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a summary
  <br><br>
- <strong>PaymentTerminalTransactionSummariesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_terminals_transaction_summaries_id_receipt</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/terminals/transaction-summaries/{id}/receipt
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a rendered summary receipt
  <br><br>
- <strong>PaymentTerminalTransactionSummariesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_terminals_transaction_summaries_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/terminals/transaction-summaries/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search summaries
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_terminals_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/terminals/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a payment terminal
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_terminals</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/terminals
  &nbsp;&nbsp;&nbsp;&nbsp;List all payment terminals
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_terminals_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/terminals/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment terminal
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_terminals_id_till_connection_credentials</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/terminals/{id}/till-connection-credentials
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve till connection credentials
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_terminals_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/terminals/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search payment terminals
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_terminals_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/terminals/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a payment terminal
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_terminals</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/terminals
  &nbsp;&nbsp;&nbsp;&nbsp;Create a payment terminal
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_terminals_by_identifier_identifier_perform_transaction</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/terminals/by-identifier/{identifier}/perform-transaction
  &nbsp;&nbsp;&nbsp;&nbsp;Perform a payment terminal transaction by identifier
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_terminals_by_identifier_identifier_trigger_final_balance</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/terminals/by-identifier/{identifier}/trigger-final-balance
  &nbsp;&nbsp;&nbsp;&nbsp;Remotely trigger the final balance by identifier
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_terminals_id_link</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/terminals/{id}/link
  &nbsp;&nbsp;&nbsp;&nbsp;Link a device with a payment terminal
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_terminals_id_perform_transaction</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/terminals/{id}/perform-transaction
  &nbsp;&nbsp;&nbsp;&nbsp;Perform a payment terminal transaction
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_terminals_id_trigger_final_balance</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/terminals/{id}/trigger-final-balance
  &nbsp;&nbsp;&nbsp;&nbsp;Remotely trigger the final balance
  <br><br>
- <strong>PaymentTerminalsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_terminals_id_unlink</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/terminals/{id}/unlink
  &nbsp;&nbsp;&nbsp;&nbsp;Unlink any device from a payment terminal
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_web_apps_connectors_connector_external_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/web-apps/connectors/{connectorExternalId}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a connector
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_web_apps_processors_external_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/web-apps/processors/{externalId}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a processor
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_web_apps_charge_attempts_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/web-apps/charge-attempts/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a charge attempt
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_web_apps_completions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/web-apps/completions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a completion
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_web_apps_connectors_connector_external_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/web-apps/connectors/{connectorExternalId}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a connector
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_web_apps_processors_external_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/web-apps/processors/{externalId}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a processor
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_web_apps_refunds_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/web-apps/refunds/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a refund
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_web_apps_voids_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/web-apps/voids/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a void
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_web_apps_processors</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/web-apps/processors
  &nbsp;&nbsp;&nbsp;&nbsp;Create a processor
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_web_apps_processors_external_id_activate_for_production</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/web-apps/processors/{externalId}/activate-for-production
  &nbsp;&nbsp;&nbsp;&nbsp;Activate a processor for production
  <br><br>
- <strong>PaymentWebAppsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_web_apps_processors_external_id_connectors</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/web-apps/processors/{externalId}/connectors
  &nbsp;&nbsp;&nbsp;&nbsp;Create a connector
  <br><br>
- <strong>PermissionsService</strong><br>
  &nbsp;&nbsp;* <code>get_permissions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /permissions
  &nbsp;&nbsp;&nbsp;&nbsp;List all permissions
  <br><br>
- <strong>PermissionsService</strong><br>
  &nbsp;&nbsp;* <code>get_permissions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /permissions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a permission
  <br><br>
- <strong>PermissionsService</strong><br>
  &nbsp;&nbsp;* <code>get_permissions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /permissions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search permissions
  <br><br>
- <strong>RefundBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_refunds</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/refunds
  &nbsp;&nbsp;&nbsp;&nbsp;List all refund bank transactions
  <br><br>
- <strong>RefundBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_refunds_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/refunds/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a refund bank transaction
  <br><br>
- <strong>RefundBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_refunds_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/refunds/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search refund bank transactions
  <br><br>
- <strong>RefundCommentsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_refunds_refund_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/refunds/{refundId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a refund comment
  <br><br>
- <strong>RefundCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_refunds_refund_id_comments</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/refunds/{refundId}/comments
  &nbsp;&nbsp;&nbsp;&nbsp;List all refund comments
  <br><br>
- <strong>RefundCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_refunds_refund_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/refunds/{refundId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a refund comment
  <br><br>
- <strong>RefundCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_refunds_refund_id_comments_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/refunds/{refundId}/comments/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search refund comments
  <br><br>
- <strong>RefundCommentsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_refunds_refund_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/refunds/{refundId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a refund comment
  <br><br>
- <strong>RefundCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_refunds_refund_id_comments</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/refunds/{refundId}/comments
  &nbsp;&nbsp;&nbsp;&nbsp;Create a refund comment
  <br><br>
- <strong>RefundCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_refunds_refund_id_comments_id_pin</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/refunds/{refundId}/comments/{id}/pin
  &nbsp;&nbsp;&nbsp;&nbsp;Pin a comment to the top
  <br><br>
- <strong>RefundCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_refunds_refund_id_comments_id_unpin</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/refunds/{refundId}/comments/{id}/unpin
  &nbsp;&nbsp;&nbsp;&nbsp;Remove the pinned comment from the top
  <br><br>
- <strong>RefundRecoveryBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_refund_recoveries</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/refund-recoveries
  &nbsp;&nbsp;&nbsp;&nbsp;List all refund recovery bank transactions
  <br><br>
- <strong>RefundRecoveryBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_refund_recoveries_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/refund-recoveries/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a refund recovery bank transaction
  <br><br>
- <strong>RefundRecoveryBankTransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_bank_transactions_refund_recoveries_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/bank-transactions/refund-recoveries/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search refund recovery bank transactions
  <br><br>
- <strong>RefundsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_refunds</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/refunds
  &nbsp;&nbsp;&nbsp;&nbsp;List all refunds
  <br><br>
- <strong>RefundsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_refunds_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/refunds/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a refund
  <br><br>
- <strong>RefundsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_refunds_id_document</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/refunds/{id}/document
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a refund document
  <br><br>
- <strong>RefundsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_refunds_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/refunds/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search refunds
  <br><br>
- <strong>RefundsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_refunds</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/refunds
  &nbsp;&nbsp;&nbsp;&nbsp;Create a refund
  <br><br>
- <strong>RefundsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_refunds_id_mark_failed</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/refunds/{id}/mark-failed
  &nbsp;&nbsp;&nbsp;&nbsp;Mark a refund as failed
  <br><br>
- <strong>RefundsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_refunds_id_mark_succeeded</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/refunds/{id}/mark-succeeded
  &nbsp;&nbsp;&nbsp;&nbsp;Mark a refund as successful
  <br><br>
- <strong>RolesService</strong><br>
  &nbsp;&nbsp;* <code>delete_roles_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /roles/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a role
  <br><br>
- <strong>RolesService</strong><br>
  &nbsp;&nbsp;* <code>get_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /roles
  &nbsp;&nbsp;&nbsp;&nbsp;List all roles
  <br><br>
- <strong>RolesService</strong><br>
  &nbsp;&nbsp;* <code>get_roles_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /roles/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a role
  <br><br>
- <strong>RolesService</strong><br>
  &nbsp;&nbsp;* <code>get_roles_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /roles/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search roles
  <br><br>
- <strong>RolesService</strong><br>
  &nbsp;&nbsp;* <code>patch_roles_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /roles/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a role
  <br><br>
- <strong>RolesService</strong><br>
  &nbsp;&nbsp;* <code>post_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /roles
  &nbsp;&nbsp;&nbsp;&nbsp;Create a role
  <br><br>
- <strong>SingleSignOnUsersService</strong><br>
  &nbsp;&nbsp;* <code>delete_single_sign_on_users_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /single-sign-on-users/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a single sign-on user
  <br><br>
- <strong>SingleSignOnUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_single_sign_on_users</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /single-sign-on-users
  &nbsp;&nbsp;&nbsp;&nbsp;List all single sign-on users
  <br><br>
- <strong>SingleSignOnUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_single_sign_on_users_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /single-sign-on-users/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a single sign-on user
  <br><br>
- <strong>SingleSignOnUsersService</strong><br>
  &nbsp;&nbsp;* <code>get_single_sign_on_users_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /single-sign-on-users/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search single sign-on users
  <br><br>
- <strong>SingleSignOnUsersService</strong><br>
  &nbsp;&nbsp;* <code>patch_single_sign_on_users_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /single-sign-on-users/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a single sign-on user
  <br><br>
- <strong>SingleSignOnUsersService</strong><br>
  &nbsp;&nbsp;* <code>post_single_sign_on_users</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /single-sign-on-users
  &nbsp;&nbsp;&nbsp;&nbsp;Create a single sign-on user
  <br><br>
- <strong>SingleSignOnUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>delete_single_sign_on_users_user_id_account_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /single-sign-on-users/{userId}/account-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Unassign a role from a single sign-on user for an account
  <br><br>
- <strong>SingleSignOnUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>delete_single_sign_on_users_user_id_space_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /single-sign-on-users/{userId}/space-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Unassign a role from a single sign-on user for a space
  <br><br>
- <strong>SingleSignOnUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>get_single_sign_on_users_user_id_account_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /single-sign-on-users/{userId}/account-roles
  &nbsp;&nbsp;&nbsp;&nbsp;List all roles of a single sign-on user for an account
  <br><br>
- <strong>SingleSignOnUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>get_single_sign_on_users_user_id_space_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /single-sign-on-users/{userId}/space-roles
  &nbsp;&nbsp;&nbsp;&nbsp;List all roles of a single sign-on user for a space
  <br><br>
- <strong>SingleSignOnUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>post_single_sign_on_users_user_id_account_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /single-sign-on-users/{userId}/account-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Assign a role to a single sign-on user for an account
  <br><br>
- <strong>SingleSignOnUsersRolesService</strong><br>
  &nbsp;&nbsp;* <code>post_single_sign_on_users_user_id_space_roles</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /single-sign-on-users/{userId}/space-roles
  &nbsp;&nbsp;&nbsp;&nbsp;Assign a role to a single sign-on user for a space
  <br><br>
- <strong>SpacesService</strong><br>
  &nbsp;&nbsp;* <code>delete_spaces_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /spaces/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a space
  <br><br>
- <strong>SpacesService</strong><br>
  &nbsp;&nbsp;* <code>get_spaces</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /spaces
  &nbsp;&nbsp;&nbsp;&nbsp;List all spaces
  <br><br>
- <strong>SpacesService</strong><br>
  &nbsp;&nbsp;* <code>get_spaces_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /spaces/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a space
  <br><br>
- <strong>SpacesService</strong><br>
  &nbsp;&nbsp;* <code>get_spaces_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /spaces/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search spaces
  <br><br>
- <strong>SpacesService</strong><br>
  &nbsp;&nbsp;* <code>patch_spaces_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /spaces/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a space
  <br><br>
- <strong>SpacesService</strong><br>
  &nbsp;&nbsp;* <code>post_spaces</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /spaces
  &nbsp;&nbsp;&nbsp;&nbsp;Create a space
  <br><br>
- <strong>StaticValuesService</strong><br>
  &nbsp;&nbsp;* <code>get_static_values</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /static-values
  &nbsp;&nbsp;&nbsp;&nbsp;List all static values
  <br><br>
- <strong>StaticValuesService</strong><br>
  &nbsp;&nbsp;* <code>get_static_values_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /static-values/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a static value
  <br><br>
- <strong>StaticValuesService</strong><br>
  &nbsp;&nbsp;* <code>get_static_values_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /static-values/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search static values
  <br><br>
- <strong>SubscribersService</strong><br>
  &nbsp;&nbsp;* <code>delete_subscriptions_subscribers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /subscriptions/subscribers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a subscriber
  <br><br>
- <strong>SubscribersService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_subscribers</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/subscribers
  &nbsp;&nbsp;&nbsp;&nbsp;List all subscribers
  <br><br>
- <strong>SubscribersService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_subscribers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/subscribers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a subscriber
  <br><br>
- <strong>SubscribersService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_subscribers_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/subscribers/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search subscribers
  <br><br>
- <strong>SubscribersService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_subscribers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/subscribers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a subscriber
  <br><br>
- <strong>SubscribersService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_subscribers</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/subscribers
  &nbsp;&nbsp;&nbsp;&nbsp;Create a subscriber
  <br><br>
- <strong>SubscriptionAffiliatesService</strong><br>
  &nbsp;&nbsp;* <code>delete_subscriptions_affiliates_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /subscriptions/affiliates/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete an affiliate
  <br><br>
- <strong>SubscriptionAffiliatesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_affiliates</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/affiliates
  &nbsp;&nbsp;&nbsp;&nbsp;List all affiliates
  <br><br>
- <strong>SubscriptionAffiliatesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_affiliates_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/affiliates/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve an affiliate
  <br><br>
- <strong>SubscriptionAffiliatesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_affiliates_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/affiliates/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search affiliates
  <br><br>
- <strong>SubscriptionAffiliatesService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_affiliates_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/affiliates/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update an affiliate
  <br><br>
- <strong>SubscriptionAffiliatesService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_affiliates</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/affiliates
  &nbsp;&nbsp;&nbsp;&nbsp;Create an affiliate
  <br><br>
- <strong>SubscriptionChargesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_charges</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/charges
  &nbsp;&nbsp;&nbsp;&nbsp;List all charges
  <br><br>
- <strong>SubscriptionChargesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_charges_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/charges/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a charge
  <br><br>
- <strong>SubscriptionChargesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_charges_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/charges/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search charges
  <br><br>
- <strong>SubscriptionChargesService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_charges</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/charges
  &nbsp;&nbsp;&nbsp;&nbsp;Create a charge
  <br><br>
- <strong>SubscriptionChargesService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_charges_id_discard</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/charges/{id}/discard
  &nbsp;&nbsp;&nbsp;&nbsp;Discard a charge
  <br><br>
- <strong>SubscriptionLedgerEntriesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_ledger_entries</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/ledger-entries
  &nbsp;&nbsp;&nbsp;&nbsp;List all ledger entries
  <br><br>
- <strong>SubscriptionLedgerEntriesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_ledger_entries_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/ledger-entries/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a ledger entry
  <br><br>
- <strong>SubscriptionLedgerEntriesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_ledger_entries_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/ledger-entries/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search ledger entries
  <br><br>
- <strong>SubscriptionLedgerEntriesService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_ledger_entries</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/ledger-entries
  &nbsp;&nbsp;&nbsp;&nbsp;Create a ledger entry
  <br><br>
- <strong>SubscriptionMetricUsageReportsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_metric_usage_reports</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/metric-usage-reports
  &nbsp;&nbsp;&nbsp;&nbsp;List all metric usage reports
  <br><br>
- <strong>SubscriptionMetricUsageReportsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_metric_usage_reports_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/metric-usage-reports/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a metric usage report
  <br><br>
- <strong>SubscriptionMetricUsageReportsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_metric_usage_reports_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/metric-usage-reports/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search metric usage reports
  <br><br>
- <strong>SubscriptionMetricUsageReportsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_metric_usage_reports</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/metric-usage-reports
  &nbsp;&nbsp;&nbsp;&nbsp;Create a metric usage report
  <br><br>
- <strong>SubscriptionMetricsService</strong><br>
  &nbsp;&nbsp;* <code>delete_subscriptions_metrics_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /subscriptions/metrics/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a metric
  <br><br>
- <strong>SubscriptionMetricsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_metrics</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/metrics
  &nbsp;&nbsp;&nbsp;&nbsp;List all metrics
  <br><br>
- <strong>SubscriptionMetricsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_metrics_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/metrics/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a metric
  <br><br>
- <strong>SubscriptionMetricsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_metrics_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/metrics/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search metrics
  <br><br>
- <strong>SubscriptionMetricsService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_metrics_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/metrics/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a metric
  <br><br>
- <strong>SubscriptionMetricsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_metrics</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/metrics
  &nbsp;&nbsp;&nbsp;&nbsp;Create a metric
  <br><br>
- <strong>SubscriptionPeriodBillsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_period_bills</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/period-bills
  &nbsp;&nbsp;&nbsp;&nbsp;List all subscription period bills
  <br><br>
- <strong>SubscriptionPeriodBillsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_period_bills_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/period-bills/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a subscription period bill
  <br><br>
- <strong>SubscriptionPeriodBillsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_period_bills_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/period-bills/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search subscription period bills
  <br><br>
- <strong>SubscriptionPeriodBillsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_period_bills_id_close</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/period-bills/{id}/close
  &nbsp;&nbsp;&nbsp;&nbsp;Close a subscription period bill
  <br><br>
- <strong>SubscriptionProductComponentGroupsService</strong><br>
  &nbsp;&nbsp;* <code>delete_subscriptions_products_component_groups_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /subscriptions/products/component-groups/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a component group
  <br><br>
- <strong>SubscriptionProductComponentGroupsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_component_groups</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/component-groups
  &nbsp;&nbsp;&nbsp;&nbsp;List all component groups
  <br><br>
- <strong>SubscriptionProductComponentGroupsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_component_groups_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/component-groups/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a component group
  <br><br>
- <strong>SubscriptionProductComponentGroupsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_component_groups_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/component-groups/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search component groups
  <br><br>
- <strong>SubscriptionProductComponentGroupsService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_products_component_groups_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/products/component-groups/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a component group
  <br><br>
- <strong>SubscriptionProductComponentGroupsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_component_groups</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/component-groups
  &nbsp;&nbsp;&nbsp;&nbsp;Create a component group
  <br><br>
- <strong>SubscriptionProductComponentsService</strong><br>
  &nbsp;&nbsp;* <code>delete_subscriptions_products_components_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /subscriptions/products/components/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a component
  <br><br>
- <strong>SubscriptionProductComponentsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_components</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/components
  &nbsp;&nbsp;&nbsp;&nbsp;List all components
  <br><br>
- <strong>SubscriptionProductComponentsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_components_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/components/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a component
  <br><br>
- <strong>SubscriptionProductComponentsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_components_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/components/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search components
  <br><br>
- <strong>SubscriptionProductComponentsService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_products_components_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/products/components/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a component
  <br><br>
- <strong>SubscriptionProductComponentsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_components</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/components
  &nbsp;&nbsp;&nbsp;&nbsp;Create a component
  <br><br>
- <strong>SubscriptionProductMeteredFeeTiersService</strong><br>
  &nbsp;&nbsp;* <code>delete_subscriptions_products_metered_fees_fee_id_tiers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /subscriptions/products/metered-fees/{feeId}/tiers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a metered fee tier
  <br><br>
- <strong>SubscriptionProductMeteredFeeTiersService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_metered_fees_fee_id_tiers</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/metered-fees/{feeId}/tiers
  &nbsp;&nbsp;&nbsp;&nbsp;List all metered fee tiers
  <br><br>
- <strong>SubscriptionProductMeteredFeeTiersService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_metered_fees_fee_id_tiers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/metered-fees/{feeId}/tiers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a metered fee tier
  <br><br>
- <strong>SubscriptionProductMeteredFeeTiersService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_metered_fees_fee_id_tiers_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/metered-fees/{feeId}/tiers/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search metered fee tiers
  <br><br>
- <strong>SubscriptionProductMeteredFeeTiersService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_products_metered_fees_fee_id_tiers_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/products/metered-fees/{feeId}/tiers/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a metered fee tier
  <br><br>
- <strong>SubscriptionProductMeteredFeeTiersService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_metered_fees_fee_id_tiers</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/metered-fees/{feeId}/tiers
  &nbsp;&nbsp;&nbsp;&nbsp;Create a metered fee tier
  <br><br>
- <strong>SubscriptionProductMeteredFeesService</strong><br>
  &nbsp;&nbsp;* <code>delete_subscriptions_products_metered_fees_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /subscriptions/products/metered-fees/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a metered fee
  <br><br>
- <strong>SubscriptionProductMeteredFeesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_metered_fees</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/metered-fees
  &nbsp;&nbsp;&nbsp;&nbsp;List all metered fees
  <br><br>
- <strong>SubscriptionProductMeteredFeesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_metered_fees_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/metered-fees/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a metered fee
  <br><br>
- <strong>SubscriptionProductMeteredFeesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_metered_fees_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/metered-fees/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search metered fees
  <br><br>
- <strong>SubscriptionProductMeteredFeesService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_products_metered_fees_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/products/metered-fees/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a metered fee
  <br><br>
- <strong>SubscriptionProductMeteredFeesService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_metered_fees</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/metered-fees
  &nbsp;&nbsp;&nbsp;&nbsp;Create a metered fee
  <br><br>
- <strong>SubscriptionProductPeriodFeesService</strong><br>
  &nbsp;&nbsp;* <code>delete_subscriptions_products_period_fees_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /subscriptions/products/period-fees/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a period fee
  <br><br>
- <strong>SubscriptionProductPeriodFeesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_period_fees</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/period-fees
  &nbsp;&nbsp;&nbsp;&nbsp;List all period fees
  <br><br>
- <strong>SubscriptionProductPeriodFeesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_period_fees_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/period-fees/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a period fee
  <br><br>
- <strong>SubscriptionProductPeriodFeesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_period_fees_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/period-fees/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search period fees
  <br><br>
- <strong>SubscriptionProductPeriodFeesService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_products_period_fees_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/products/period-fees/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a period fee
  <br><br>
- <strong>SubscriptionProductPeriodFeesService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_period_fees</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/period-fees
  &nbsp;&nbsp;&nbsp;&nbsp;Create a period fee
  <br><br>
- <strong>SubscriptionProductRetirementsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_retirements</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/retirements
  &nbsp;&nbsp;&nbsp;&nbsp;List all product retirements
  <br><br>
- <strong>SubscriptionProductRetirementsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_retirements_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/retirements/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a product retirement
  <br><br>
- <strong>SubscriptionProductRetirementsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_retirements_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/retirements/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search product retirements
  <br><br>
- <strong>SubscriptionProductSetupFeesService</strong><br>
  &nbsp;&nbsp;* <code>delete_subscriptions_products_setup_fees_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /subscriptions/products/setup-fees/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a setup fee
  <br><br>
- <strong>SubscriptionProductSetupFeesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_setup_fees</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/setup-fees
  &nbsp;&nbsp;&nbsp;&nbsp;List all setup fees
  <br><br>
- <strong>SubscriptionProductSetupFeesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_setup_fees_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/setup-fees/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a setup fee
  <br><br>
- <strong>SubscriptionProductSetupFeesService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_setup_fees_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/setup-fees/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search setup fees
  <br><br>
- <strong>SubscriptionProductSetupFeesService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_products_setup_fees_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/products/setup-fees/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a setup fee
  <br><br>
- <strong>SubscriptionProductSetupFeesService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_setup_fees</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/setup-fees
  &nbsp;&nbsp;&nbsp;&nbsp;Create a setup fee
  <br><br>
- <strong>SubscriptionProductVersionRetirementsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_versions_retirements</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/versions/retirements
  &nbsp;&nbsp;&nbsp;&nbsp;List all product version retirements
  <br><br>
- <strong>SubscriptionProductVersionRetirementsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_versions_retirements_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/versions/retirements/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a product version retirement
  <br><br>
- <strong>SubscriptionProductVersionRetirementsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_versions_retirements_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/versions/retirements/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search product version retirements
  <br><br>
- <strong>SubscriptionProductVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_versions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/versions
  &nbsp;&nbsp;&nbsp;&nbsp;List all product versions
  <br><br>
- <strong>SubscriptionProductVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_versions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/versions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a product version
  <br><br>
- <strong>SubscriptionProductVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_versions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/versions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search product versions
  <br><br>
- <strong>SubscriptionProductVersionsService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_products_versions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/products/versions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a product version
  <br><br>
- <strong>SubscriptionProductVersionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_versions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/versions
  &nbsp;&nbsp;&nbsp;&nbsp;Create a product version
  <br><br>
- <strong>SubscriptionProductVersionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_versions_id_activate</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/versions/{id}/activate
  &nbsp;&nbsp;&nbsp;&nbsp;Activate a product version
  <br><br>
- <strong>SubscriptionProductVersionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_versions_id_retire</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/versions/{id}/retire
  &nbsp;&nbsp;&nbsp;&nbsp;Retire a product version
  <br><br>
- <strong>SubscriptionProductsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products
  &nbsp;&nbsp;&nbsp;&nbsp;List all products
  <br><br>
- <strong>SubscriptionProductsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a product
  <br><br>
- <strong>SubscriptionProductsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_products_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/products/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search products
  <br><br>
- <strong>SubscriptionProductsService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_products_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/products/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a product
  <br><br>
- <strong>SubscriptionProductsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products
  &nbsp;&nbsp;&nbsp;&nbsp;Create a product
  <br><br>
- <strong>SubscriptionProductsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_products_id_retire</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/products/{id}/retire
  &nbsp;&nbsp;&nbsp;&nbsp;Retire a product
  <br><br>
- <strong>SubscriptionSuspensionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_suspensions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/suspensions
  &nbsp;&nbsp;&nbsp;&nbsp;List all suspensions
  <br><br>
- <strong>SubscriptionSuspensionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_suspensions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/suspensions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a suspension
  <br><br>
- <strong>SubscriptionSuspensionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_suspensions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/suspensions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search suspensions
  <br><br>
- <strong>SubscriptionVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_versions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/versions
  &nbsp;&nbsp;&nbsp;&nbsp;List all subscription versions
  <br><br>
- <strong>SubscriptionVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_versions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/versions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a subscription version
  <br><br>
- <strong>SubscriptionVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_versions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/versions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search subscription versions
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions
  &nbsp;&nbsp;&nbsp;&nbsp;List all subscriptions
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a subscription
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_id_invoices</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/{id}/invoices
  &nbsp;&nbsp;&nbsp;&nbsp;Search subscription invoices
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>get_subscriptions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /subscriptions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search subscriptions
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>patch_subscriptions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /subscriptions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a subscription
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions
  &nbsp;&nbsp;&nbsp;&nbsp;Create a subscription
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_id_apply_changes</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/{id}/apply-changes
  &nbsp;&nbsp;&nbsp;&nbsp;Apply changes to a subscription
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_id_initialize</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/{id}/initialize
  &nbsp;&nbsp;&nbsp;&nbsp;Initialize a subscription
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_id_initialize_subscriber_present</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/{id}/initialize-subscriber-present
  &nbsp;&nbsp;&nbsp;&nbsp;Initialize a subscription with the subscriber present
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_id_reactivate</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/{id}/reactivate
  &nbsp;&nbsp;&nbsp;&nbsp;Reactivate a suspended subscription
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_id_suspend</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/{id}/suspend
  &nbsp;&nbsp;&nbsp;&nbsp;Suspend a subscription
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_id_terminate</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/{id}/terminate
  &nbsp;&nbsp;&nbsp;&nbsp;Terminate a subscription
  <br><br>
- <strong>SubscriptionsService</strong><br>
  &nbsp;&nbsp;* <code>post_subscriptions_id_upgrade_product</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /subscriptions/{id}/upgrade-product
  &nbsp;&nbsp;&nbsp;&nbsp;Upgrade a subscription&#39;s product
  <br><br>
- <strong>TokenVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_token_versions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/token-versions
  &nbsp;&nbsp;&nbsp;&nbsp;List all token versions
  <br><br>
- <strong>TokenVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_token_versions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/token-versions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a token version
  <br><br>
- <strong>TokenVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_token_versions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/token-versions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search token token versions
  <br><br>
- <strong>TokensService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_tokens_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/tokens/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a token
  <br><br>
- <strong>TokensService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_tokens</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/tokens
  &nbsp;&nbsp;&nbsp;&nbsp;List all tokens
  <br><br>
- <strong>TokensService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_tokens_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/tokens/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a token
  <br><br>
- <strong>TokensService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_tokens_id_active_version</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/tokens/{id}/active-version
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve the active token version
  <br><br>
- <strong>TokensService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_tokens_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/tokens/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search tokens
  <br><br>
- <strong>TokensService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_tokens_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/tokens/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a token
  <br><br>
- <strong>TokensService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_tokens</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/tokens
  &nbsp;&nbsp;&nbsp;&nbsp;Create a token
  <br><br>
- <strong>TokensService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_tokens_id_create_transaction_for_token_update</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/tokens/{id}/create-transaction-for-token-update
  &nbsp;&nbsp;&nbsp;&nbsp;Create a transaction for token update
  <br><br>
- <strong>TransactionClientPlatformsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transaction_client_platforms</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transaction/client-platforms
  &nbsp;&nbsp;&nbsp;&nbsp;List all client platforms
  <br><br>
- <strong>TransactionClientPlatformsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transaction_client_platforms_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transaction/client-platforms/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve the client platform based on id
  <br><br>
- <strong>TransactionClientPlatformsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transaction_client_platforms_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transaction/client-platforms/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search client platforms
  <br><br>
- <strong>TransactionCommentsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_transactions_transaction_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/transactions/{transactionId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a transaction comment
  <br><br>
- <strong>TransactionCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_transaction_id_comments</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{transactionId}/comments
  &nbsp;&nbsp;&nbsp;&nbsp;List all transaction comments
  <br><br>
- <strong>TransactionCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_transaction_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{transactionId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a transaction comment
  <br><br>
- <strong>TransactionCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_transaction_id_comments_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{transactionId}/comments/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search transaction comments
  <br><br>
- <strong>TransactionCommentsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_transactions_transaction_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/transactions/{transactionId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a transaction comment
  <br><br>
- <strong>TransactionCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_transaction_id_comments</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{transactionId}/comments
  &nbsp;&nbsp;&nbsp;&nbsp;Create a transaction comment
  <br><br>
- <strong>TransactionCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_transaction_id_comments_id_pin</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{transactionId}/comments/{id}/pin
  &nbsp;&nbsp;&nbsp;&nbsp;Pin a comment to the top
  <br><br>
- <strong>TransactionCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_transaction_id_comments_id_unpin</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{transactionId}/comments/{id}/unpin
  &nbsp;&nbsp;&nbsp;&nbsp;Remove the pinned comment from the top
  <br><br>
- <strong>TransactionCompletionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_completions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/completions
  &nbsp;&nbsp;&nbsp;&nbsp;List all transaction completions
  <br><br>
- <strong>TransactionCompletionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_completions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/completions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a transaction completion
  <br><br>
- <strong>TransactionCompletionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_completions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/completions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search transaction completions
  <br><br>
- <strong>TransactionInvoiceCommentsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_transactions_invoices_invoice_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/transactions/invoices/{invoiceId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a transaction comment
  <br><br>
- <strong>TransactionInvoiceCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_invoices_invoice_id_comments</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/invoices/{invoiceId}/comments
  &nbsp;&nbsp;&nbsp;&nbsp;List all transaction invoice comments
  <br><br>
- <strong>TransactionInvoiceCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_invoices_invoice_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/invoices/{invoiceId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a transaction invoice comment
  <br><br>
- <strong>TransactionInvoiceCommentsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_invoices_invoice_id_comments_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/invoices/{invoiceId}/comments/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search transaction invoice comments
  <br><br>
- <strong>TransactionInvoiceCommentsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_transactions_invoices_invoice_id_comments_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/transactions/invoices/{invoiceId}/comments/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a transaction comment
  <br><br>
- <strong>TransactionInvoiceCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_invoices_invoice_id_comments</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/invoices/{invoiceId}/comments
  &nbsp;&nbsp;&nbsp;&nbsp;Create a transaction invoice comment
  <br><br>
- <strong>TransactionInvoiceCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_invoices_invoice_id_comments_id_pin</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/invoices/{invoiceId}/comments/{id}/pin
  &nbsp;&nbsp;&nbsp;&nbsp;Pin a comment to the top
  <br><br>
- <strong>TransactionInvoiceCommentsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_invoices_invoice_id_comments_id_unpin</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/invoices/{invoiceId}/comments/{id}/unpin
  &nbsp;&nbsp;&nbsp;&nbsp;Remove the pinned comment from the top
  <br><br>
- <strong>TransactionInvoicesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_invoices</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/invoices
  &nbsp;&nbsp;&nbsp;&nbsp;List all transaction invoices
  <br><br>
- <strong>TransactionInvoicesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_invoices_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/invoices/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a transaction invoice
  <br><br>
- <strong>TransactionInvoicesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_invoices_id_check_replacement_possible</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/invoices/{id}/check-replacement-possible
  &nbsp;&nbsp;&nbsp;&nbsp;Check if a transaction invoice can be replaced
  <br><br>
- <strong>TransactionInvoicesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_invoices_id_document</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/invoices/{id}/document
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve an invoice document
  <br><br>
- <strong>TransactionInvoicesService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_invoices_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/invoices/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search transaction invoices
  <br><br>
- <strong>TransactionInvoicesService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_invoices_id_derecognize</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/invoices/{id}/derecognize
  &nbsp;&nbsp;&nbsp;&nbsp;Derecognize a transaction invoice
  <br><br>
- <strong>TransactionInvoicesService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_invoices_id_mark_paid</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/invoices/{id}/mark-paid
  &nbsp;&nbsp;&nbsp;&nbsp;Mark a transaction invoice as paid
  <br><br>
- <strong>TransactionInvoicesService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_invoices_id_replace</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/invoices/{id}/replace
  &nbsp;&nbsp;&nbsp;&nbsp;Replace a transaction invoice
  <br><br>
- <strong>TransactionLineItemVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_line_item_versions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/line-item-versions
  &nbsp;&nbsp;&nbsp;&nbsp;List all transaction line item versions
  <br><br>
- <strong>TransactionLineItemVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_line_item_versions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/line-item-versions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a transaction line item version
  <br><br>
- <strong>TransactionLineItemVersionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_line_item_versions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/line-item-versions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search transaction line item versions
  <br><br>
- <strong>TransactionLineItemVersionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_line_item_versions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/line-item-versions
  &nbsp;&nbsp;&nbsp;&nbsp;Create a transaction line item version
  <br><br>
- <strong>TransactionVoidsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_voids</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/voids
  &nbsp;&nbsp;&nbsp;&nbsp;List all transaction voids
  <br><br>
- <strong>TransactionVoidsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_voids_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/voids/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a transaction void
  <br><br>
- <strong>TransactionVoidsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_voids_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/voids/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search transaction voids
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>delete_payment_transactions_by_credentials_credentials_one_click_tokens_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /payment/transactions/by-credentials/{credentials}/one-click-tokens/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a one-click token by credentials
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions
  &nbsp;&nbsp;&nbsp;&nbsp;List all transactions
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_by_credentials_credentials</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/by-credentials/{credentials}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a transaction by credentials
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_by_credentials_credentials_mobile_sdk_url</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/by-credentials/{credentials}/mobile-sdk-url
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a Mobile SDK URL by credentials
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_by_credentials_credentials_one_click_tokens</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/by-credentials/{credentials}/one-click-tokens
  &nbsp;&nbsp;&nbsp;&nbsp;List one-click tokens by credentials
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_by_credentials_credentials_payment_method_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/by-credentials/{credentials}/payment-method-configurations
  &nbsp;&nbsp;&nbsp;&nbsp;List available payment method configurations by credentials
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_export</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/export
  &nbsp;&nbsp;&nbsp;&nbsp;Export transactions
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a transaction
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_charge_flow_payment_page_url</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/charge-flow/payment-page-url
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a charge flow payment page URL
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_check_token_creation_possible</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/check-token-creation-possible
  &nbsp;&nbsp;&nbsp;&nbsp;Check if token can be created
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_credentials</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/credentials
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve transaction credentials
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_iframe_javascript_url</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/iframe-javascript-url
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve an iFrame JavaScript URL
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_invoice_document</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/invoice-document
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve an invoice document
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_latest_line_item_version</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/latest-line-item-version
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve the latest line item version
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_lightbox_javascript_url</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/lightbox-javascript-url
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a Lightbox JavaScript URL
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_packing_slip_document</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/packing-slip-document
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a packing slip document
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_payment_method_configurations</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/payment-method-configurations
  &nbsp;&nbsp;&nbsp;&nbsp;List available payment method configurations
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_payment_page_url</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/payment-page-url
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a payment page URL
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_id_terminal_receipts</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/{id}/terminal-receipts
  &nbsp;&nbsp;&nbsp;&nbsp;List terminal receipts
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>get_payment_transactions_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /payment/transactions/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search transactions
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>patch_payment_transactions_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /payment/transactions/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a transaction
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions
  &nbsp;&nbsp;&nbsp;&nbsp;Create a transaction
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_by_credentials_credentials_one_click_tokens_id_process</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/by-credentials/{credentials}/one-click-tokens/{id}/process
  &nbsp;&nbsp;&nbsp;&nbsp;Process via one-click token by credentials
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_charge_flow_apply</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/charge-flow/apply
  &nbsp;&nbsp;&nbsp;&nbsp;Process a transaction via charge flow
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_charge_flow_cancel</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/charge-flow/cancel
  &nbsp;&nbsp;&nbsp;&nbsp;Cancel a charge flow
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_charge_flow_update_recipient</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/charge-flow/update-recipient
  &nbsp;&nbsp;&nbsp;&nbsp;Update a charge flow recipient
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_complete_offline</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/complete-offline
  &nbsp;&nbsp;&nbsp;&nbsp;Complete a transaction offline
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_complete_online</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/complete-online
  &nbsp;&nbsp;&nbsp;&nbsp;Complete a transaction online
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_complete_partially_offline</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/complete-partially-offline
  &nbsp;&nbsp;&nbsp;&nbsp;Complete a transaction offline partially
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_complete_partially_online</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/complete-partially-online
  &nbsp;&nbsp;&nbsp;&nbsp;Complete a transaction online partially
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_confirm</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/confirm
  &nbsp;&nbsp;&nbsp;&nbsp;Confirm a transaction
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_process_card_details</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/process-card-details
  &nbsp;&nbsp;&nbsp;&nbsp;Process a card transaction
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_process_card_details_threed</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/process-card-details-threed
  &nbsp;&nbsp;&nbsp;&nbsp;Process a card transaction with 3-D Secure
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_process_with_token</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/process-with-token
  &nbsp;&nbsp;&nbsp;&nbsp;Process a transaction via token
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_process_without_interaction</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/process-without-interaction
  &nbsp;&nbsp;&nbsp;&nbsp;Process a transaction without user-interaction
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_void_offline</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/void-offline
  &nbsp;&nbsp;&nbsp;&nbsp;Void a transaction offline
  <br><br>
- <strong>TransactionsService</strong><br>
  &nbsp;&nbsp;* <code>post_payment_transactions_id_void_online</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /payment/transactions/{id}/void-online
  &nbsp;&nbsp;&nbsp;&nbsp;Void a transaction online
  <br><br>
- <strong>WebAppsService</strong><br>
  &nbsp;&nbsp;* <code>get_web_apps_installed</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /web-apps/installed
  &nbsp;&nbsp;&nbsp;&nbsp;Check whether the web app is installed
  <br><br>
- <strong>WebAppsService</strong><br>
  &nbsp;&nbsp;* <code>post_web_apps_confirm_code</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /web-apps/confirm/{code}
  &nbsp;&nbsp;&nbsp;&nbsp;Confirm a web app installation
  <br><br>
- <strong>WebAppsService</strong><br>
  &nbsp;&nbsp;* <code>post_web_apps_uninstall</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /web-apps/uninstall
  &nbsp;&nbsp;&nbsp;&nbsp;Uninstall a web app
  <br><br>
- <strong>WebhookEncryptionKeysService</strong><br>
  &nbsp;&nbsp;* <code>get_webhooks_encryption_keys_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /webhooks/encryption-keys/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a webhook encryption key
  <br><br>
- <strong>WebhookListenersService</strong><br>
  &nbsp;&nbsp;* <code>delete_webhooks_listeners_bulk</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /webhooks/listeners/bulk
  &nbsp;&nbsp;&nbsp;&nbsp;Delete multiple webhook listeners
  <br><br>
- <strong>WebhookListenersService</strong><br>
  &nbsp;&nbsp;* <code>delete_webhooks_listeners_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /webhooks/listeners/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a webhook listener
  <br><br>
- <strong>WebhookListenersService</strong><br>
  &nbsp;&nbsp;* <code>get_webhooks_listeners</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /webhooks/listeners
  &nbsp;&nbsp;&nbsp;&nbsp;List all webhook listeners
  <br><br>
- <strong>WebhookListenersService</strong><br>
  &nbsp;&nbsp;* <code>get_webhooks_listeners_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /webhooks/listeners/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a webhook listener
  <br><br>
- <strong>WebhookListenersService</strong><br>
  &nbsp;&nbsp;* <code>get_webhooks_listeners_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /webhooks/listeners/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search webhook listeners
  <br><br>
- <strong>WebhookListenersService</strong><br>
  &nbsp;&nbsp;* <code>patch_webhooks_listeners_bulk</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /webhooks/listeners/bulk
  &nbsp;&nbsp;&nbsp;&nbsp;Update multiple webhook listeners
  <br><br>
- <strong>WebhookListenersService</strong><br>
  &nbsp;&nbsp;* <code>patch_webhooks_listeners_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /webhooks/listeners/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a webhook listener
  <br><br>
- <strong>WebhookListenersService</strong><br>
  &nbsp;&nbsp;* <code>post_webhooks_listeners</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /webhooks/listeners
  &nbsp;&nbsp;&nbsp;&nbsp;Create a webhook listener
  <br><br>
- <strong>WebhookListenersService</strong><br>
  &nbsp;&nbsp;* <code>post_webhooks_listeners_bulk</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /webhooks/listeners/bulk
  &nbsp;&nbsp;&nbsp;&nbsp;Create multiple webhook listeners
  <br><br>
- <strong>WebhookURLsService</strong><br>
  &nbsp;&nbsp;* <code>delete_webhooks_urls_bulk</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /webhooks/urls/bulk
  &nbsp;&nbsp;&nbsp;&nbsp;Delete multiple webhook URLs
  <br><br>
- <strong>WebhookURLsService</strong><br>
  &nbsp;&nbsp;* <code>delete_webhooks_urls_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>DELETE</strong> /webhooks/urls/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Delete a webhook URL
  <br><br>
- <strong>WebhookURLsService</strong><br>
  &nbsp;&nbsp;* <code>get_webhooks_urls</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /webhooks/urls
  &nbsp;&nbsp;&nbsp;&nbsp;List all webhook URLs
  <br><br>
- <strong>WebhookURLsService</strong><br>
  &nbsp;&nbsp;* <code>get_webhooks_urls_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /webhooks/urls/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Retrieve a webhook URL
  <br><br>
- <strong>WebhookURLsService</strong><br>
  &nbsp;&nbsp;* <code>get_webhooks_urls_search</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>GET</strong> /webhooks/urls/search
  &nbsp;&nbsp;&nbsp;&nbsp;Search webhook URLs
  <br><br>
- <strong>WebhookURLsService</strong><br>
  &nbsp;&nbsp;* <code>patch_webhooks_urls_bulk</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /webhooks/urls/bulk
  &nbsp;&nbsp;&nbsp;&nbsp;Update multiple webhook URLs
  <br><br>
- <strong>WebhookURLsService</strong><br>
  &nbsp;&nbsp;* <code>patch_webhooks_urls_id</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>PATCH</strong> /webhooks/urls/{id}
  &nbsp;&nbsp;&nbsp;&nbsp;Update a webhook URL
  <br><br>
- <strong>WebhookURLsService</strong><br>
  &nbsp;&nbsp;* <code>post_webhooks_urls</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /webhooks/urls
  &nbsp;&nbsp;&nbsp;&nbsp;Create a webhook URL
  <br><br>
- <strong>WebhookURLsService</strong><br>
  &nbsp;&nbsp;* <code>post_webhooks_urls_bulk</code>
  &nbsp;&nbsp;&nbsp;&nbsp;<strong>POST</strong> /webhooks/urls/bulk
  &nbsp;&nbsp;&nbsp;&nbsp;Create multiple webhook URLs
  <br><br>

</details>

## Documentation for Models
Additional Api models documentation: [*link*](https://app-wallee.com/en-us/doc/api/web-service#_models)<br>
<details>
<summary>Click here to see full list of models</summary>

<p><strong>Models:</strong></p>

* <strong>AbstractAccountUpdate</strong>
* <strong>AbstractApplicationUserUpdate</strong>
* <strong>AbstractCustomerActive</strong>
* <strong>AbstractCustomerAddressActive</strong>
* <strong>AbstractCustomerCommentActive</strong>
* <strong>AbstractDebtCollectionCaseUpdate</strong>
* <strong>AbstractDebtCollectorConfigurationUpdate</strong>
* <strong>AbstractHumanUserUpdate</strong>
* <strong>AbstractPaymentConnectorConfigurationUpdate</strong>
* <strong>AbstractPaymentLinkUpdate</strong>
* <strong>AbstractPaymentMethodConfigurationUpdate</strong>
* <strong>AbstractPaymentProcessorConfigurationActive</strong>
* <strong>AbstractPaymentTerminalUpdate</strong>
* <strong>AbstractRefundCommentActive</strong>
* <strong>AbstractRoleUpdate</strong>
* <strong>AbstractSingleSignOnUserUpdate</strong>
* <strong>AbstractSpaceUpdate</strong>
* <strong>AbstractSubscriberUpdate</strong>
* <strong>AbstractSubscriptionAffiliateUpdate</strong>
* <strong>AbstractSubscriptionMetricUpdate</strong>
* <strong>AbstractSubscriptionProductActive</strong>
* <strong>AbstractTokenUpdate</strong>
* <strong>AbstractTransactionCommentActive</strong>
* <strong>AbstractTransactionInvoiceCommentActive</strong>
* <strong>AbstractTransactionPending</strong>
* <strong>AbstractWebhookListenerUpdate</strong>
* <strong>AbstractWebhookUrlUpdate</strong>
* <strong>Account</strong>
* <strong>AccountCreate</strong>
* <strong>AccountListResponse</strong>
* <strong>AccountSearchResponse</strong>
* <strong>AccountState</strong>
* <strong>AccountType</strong>
* <strong>AccountUpdate</strong>
* <strong>Address</strong>
* <strong>AddressCreate</strong>
* <strong>AnalyticsQueryExecutionRequest</strong>
* <strong>AnalyticsQueryExecutionResponse</strong>
* <strong>ApplicationKeyState</strong>
* <strong>ApplicationUser</strong>
* <strong>ApplicationUserCreate</strong>
* <strong>ApplicationUserCreateWithMacKey</strong>
* <strong>ApplicationUserListResponse</strong>
* <strong>ApplicationUserSearchResponse</strong>
* <strong>ApplicationUserUpdate</strong>
* <strong>AuthenticatedCardData</strong>
* <strong>AuthenticatedCardDataCreate</strong>
* <strong>AuthenticatedCardRequest</strong>
* <strong>BankAccount</strong>
* <strong>BankAccountEnvironment</strong>
* <strong>BankAccountListResponse</strong>
* <strong>BankAccountSearchResponse</strong>
* <strong>BankAccountState</strong>
* <strong>BankAccountType</strong>
* <strong>BankTransaction</strong>
* <strong>BankTransactionFlowDirection</strong>
* <strong>BankTransactionListResponse</strong>
* <strong>BankTransactionSearchResponse</strong>
* <strong>BankTransactionSource</strong>
* <strong>BankTransactionState</strong>
* <strong>BankTransactionType</strong>
* <strong>BillingCycleModel</strong>
* <strong>BillingCycleType</strong>
* <strong>BillingDayCustomization</strong>
* <strong>CardAuthenticationResponse</strong>
* <strong>CardAuthenticationVersion</strong>
* <strong>CardCryptogram</strong>
* <strong>CardCryptogramCreate</strong>
* <strong>CardholderAuthentication</strong>
* <strong>CardholderAuthenticationCreate</strong>
* <strong>Charge</strong>
* <strong>ChargeAttempt</strong>
* <strong>ChargeAttemptEnvironment</strong>
* <strong>ChargeAttemptListResponse</strong>
* <strong>ChargeAttemptSearchResponse</strong>
* <strong>ChargeAttemptState</strong>
* <strong>ChargeBankTransaction</strong>
* <strong>ChargeBankTransactionListResponse</strong>
* <strong>ChargeBankTransactionSearchResponse</strong>
* <strong>ChargeFlow</strong>
* <strong>ChargeFlowLevel</strong>
* <strong>ChargeFlowLevelConfiguration</strong>
* <strong>ChargeFlowLevelConfigurationType</strong>
* <strong>ChargeFlowLevelListResponse</strong>
* <strong>ChargeFlowLevelPaymentLink</strong>
* <strong>ChargeFlowLevelPaymentLinkListResponse</strong>
* <strong>ChargeFlowLevelPaymentLinkSearchResponse</strong>
* <strong>ChargeFlowLevelSearchResponse</strong>
* <strong>ChargeFlowLevelState</strong>
* <strong>ChargeFlowListResponse</strong>
* <strong>ChargeFlowSearchResponse</strong>
* <strong>ChargeState</strong>
* <strong>ChargeType</strong>
* <strong>ClientPlatformInformationListResponse</strong>
* <strong>ClientPlatformInformationSearchResponse</strong>
* <strong>CompletionLineItem</strong>
* <strong>CompletionLineItemCreate</strong>
* <strong>CompletionListResponse</strong>
* <strong>CompletionSearchResponse</strong>
* <strong>Condition</strong>
* <strong>ConditionType</strong>
* <strong>ConditionTypeListResponse</strong>
* <strong>ConditionTypeSearchResponse</strong>
* <strong>ConnectorInvocation</strong>
* <strong>ConnectorInvocationStage</strong>
* <strong>CountryListResponse</strong>
* <strong>CountrySearchResponse</strong>
* <strong>CreationEntityState</strong>
* <strong>CurrencyBankAccount</strong>
* <strong>CurrencyBankAccountListResponse</strong>
* <strong>CurrencyBankAccountSearchResponse</strong>
* <strong>CurrencyListResponse</strong>
* <strong>CurrencySearchResponse</strong>
* <strong>Customer</strong>
* <strong>CustomerActive</strong>
* <strong>CustomerAddress</strong>
* <strong>CustomerAddressActive</strong>
* <strong>CustomerAddressCreate</strong>
* <strong>CustomerAddressListResponse</strong>
* <strong>CustomerAddressSearchResponse</strong>
* <strong>CustomerAddressType</strong>
* <strong>CustomerComment</strong>
* <strong>CustomerCommentActive</strong>
* <strong>CustomerCommentCreate</strong>
* <strong>CustomerCommentListResponse</strong>
* <strong>CustomerCommentSearchResponse</strong>
* <strong>CustomerCreate</strong>
* <strong>CustomerEmailAddressListResponse</strong>
* <strong>CustomerListResponse</strong>
* <strong>CustomerPostalAddress</strong>
* <strong>CustomerPostalAddressCreate</strong>
* <strong>CustomerSearchResponse</strong>
* <strong>CustomersPresence</strong>
* <strong>DataCollectionType</strong>
* <strong>DebtCollectionCase</strong>
* <strong>DebtCollectionCaseCreate</strong>
* <strong>DebtCollectionCaseDocument</strong>
* <strong>DebtCollectionCaseDocumentListResponse</strong>
* <strong>DebtCollectionCaseListResponse</strong>
* <strong>DebtCollectionCaseSearchResponse</strong>
* <strong>DebtCollectionCaseSource</strong>
* <strong>DebtCollectionCaseState</strong>
* <strong>DebtCollectionCaseUpdate</strong>
* <strong>DebtCollectionEnvironment</strong>
* <strong>DebtCollectionReceipt</strong>
* <strong>DebtCollectionReceiptSource</strong>
* <strong>DebtCollector</strong>
* <strong>DebtCollectorCondition</strong>
* <strong>DebtCollectorConditionType</strong>
* <strong>DebtCollectorConfiguration</strong>
* <strong>DebtCollectorConfigurationCreate</strong>
* <strong>DebtCollectorConfigurationListResponse</strong>
* <strong>DebtCollectorConfigurationSearchResponse</strong>
* <strong>DebtCollectorConfigurationUpdate</strong>
* <strong>DebtCollectorListResponse</strong>
* <strong>DebtCollectorSearchResponse</strong>
* <strong>DeliveryIndication</strong>
* <strong>DeliveryIndicationDecisionReason</strong>
* <strong>DeliveryIndicationListResponse</strong>
* <strong>DeliveryIndicationSearchResponse</strong>
* <strong>DeliveryIndicationState</strong>
* <strong>DisplayableDayOfWeek</strong>
* <strong>DisplayableMonth</strong>
* <strong>DocumentTemplate</strong>
* <strong>DocumentTemplateListResponse</strong>
* <strong>DocumentTemplateSearchResponse</strong>
* <strong>DocumentTemplateType</strong>
* <strong>DocumentTemplateTypeGroup</strong>
* <strong>DocumentTemplateTypeListResponse</strong>
* <strong>DocumentTemplateTypeSearchResponse</strong>
* <strong>DunningCase</strong>
* <strong>DunningCaseListResponse</strong>
* <strong>DunningCaseSearchResponse</strong>
* <strong>DunningCaseState</strong>
* <strong>DunningCondition</strong>
* <strong>DunningConditionType</strong>
* <strong>DunningFlow</strong>
* <strong>DunningFlowLevel</strong>
* <strong>DunningFlowLevelListResponse</strong>
* <strong>DunningFlowLevelProcessor</strong>
* <strong>DunningFlowLevelSearchResponse</strong>
* <strong>DunningFlowListResponse</strong>
* <strong>DunningFlowSearchResponse</strong>
* <strong>DunningFlowType</strong>
* <strong>Environment</strong>
* <strong>ExpressCheckoutCreateResponse</strong>
* <strong>ExpressCheckoutSession</strong>
* <strong>ExpressCheckoutSessionCreate</strong>
* <strong>ExpressCheckoutSessionState</strong>
* <strong>ExpressCheckoutShippingOption</strong>
* <strong>ExpressCheckoutWalletType</strong>
* <strong>ExternalTransferBankTransaction</strong>
* <strong>ExternalTransferBankTransactionListResponse</strong>
* <strong>ExternalTransferBankTransactionSearchResponse</strong>
* <strong>FacadeUserFriendlyQueryStatusModel</strong>
* <strong>FailureCategory</strong>
* <strong>FailureReason</strong>
* <strong>Feature</strong>
* <strong>FeatureCategory</strong>
* <strong>Gender</strong>
* <strong>HumanUser</strong>
* <strong>HumanUserCreate</strong>
* <strong>HumanUserListResponse</strong>
* <strong>HumanUserSearchResponse</strong>
* <strong>HumanUserUpdate</strong>
* <strong>InternalTransferBankTransaction</strong>
* <strong>InternalTransferBankTransactionListResponse</strong>
* <strong>InternalTransferBankTransactionSearchResponse</strong>
* <strong>InvoiceCommentListResponse</strong>
* <strong>InvoiceCommentSearchResponse</strong>
* <strong>InvoiceListResponse</strong>
* <strong>InvoiceSearchResponse</strong>
* <strong>Label</strong>
* <strong>LabelDescriptor</strong>
* <strong>LabelDescriptorCategory</strong>
* <strong>LabelDescriptorGroup</strong>
* <strong>LabelDescriptorGroupListResponse</strong>
* <strong>LabelDescriptorGroupSearchResponse</strong>
* <strong>LabelDescriptorListResponse</strong>
* <strong>LabelDescriptorSearchResponse</strong>
* <strong>LabelDescriptorType</strong>
* <strong>LanguageListResponse</strong>
* <strong>LanguageSearchResponse</strong>
* <strong>LegalOrganizationForm</strong>
* <strong>LegalOrganizationFormListResponse</strong>
* <strong>LegalOrganizationFormSearchResponse</strong>
* <strong>LineItem</strong>
* <strong>LineItemAttribute</strong>
* <strong>LineItemAttributeCreate</strong>
* <strong>LineItemCreate</strong>
* <strong>LineItemReduction</strong>
* <strong>LineItemReductionCreate</strong>
* <strong>LineItemType</strong>
* <strong>LineItemVersionListResponse</strong>
* <strong>LineItemVersionSearchResponse</strong>
* <strong>LocalizedString</strong>
* <strong>ManualTask</strong>
* <strong>ManualTaskAction</strong>
* <strong>ManualTaskActionStyle</strong>
* <strong>ManualTaskListResponse</strong>
* <strong>ManualTaskSearchResponse</strong>
* <strong>ManualTaskState</strong>
* <strong>ManualTaskType</strong>
* <strong>MetricListResponse</strong>
* <strong>MetricSearchResponse</strong>
* <strong>MetricUsage</strong>
* <strong>MetricUsageListResponse</strong>
* <strong>MetricUsageReportListResponse</strong>
* <strong>MetricUsageReportSearchResponse</strong>
* <strong>OneClickPaymentMode</strong>
* <strong>PanType</strong>
* <strong>PaymentAdjustment</strong>
* <strong>PaymentAdjustmentType</strong>
* <strong>PaymentAppChargeAttemptTargetState</strong>
* <strong>PaymentAppChargeAttemptUpdate</strong>
* <strong>PaymentAppCompletionConfiguration</strong>
* <strong>PaymentAppCompletionConfigurationCreate</strong>
* <strong>PaymentAppCompletionTargetState</strong>
* <strong>PaymentAppCompletionUpdate</strong>
* <strong>PaymentAppConnector</strong>
* <strong>PaymentAppConnectorDetails</strong>
* <strong>PaymentAppConnectorDetailsCreate</strong>
* <strong>PaymentAppConnectorState</strong>
* <strong>PaymentAppProcessor</strong>
* <strong>PaymentAppProcessorDetails</strong>
* <strong>PaymentAppProcessorDetailsCreate</strong>
* <strong>PaymentAppProcessorState</strong>
* <strong>PaymentAppRefundConfiguration</strong>
* <strong>PaymentAppRefundConfigurationCreate</strong>
* <strong>PaymentAppRefundTargetState</strong>
* <strong>PaymentAppRefundUpdate</strong>
* <strong>PaymentAppVoidTargetState</strong>
* <strong>PaymentAppVoidUpdate</strong>
* <strong>PaymentConnector</strong>
* <strong>PaymentConnectorConfiguration</strong>
* <strong>PaymentConnectorConfigurationCreate</strong>
* <strong>PaymentConnectorConfigurationListResponse</strong>
* <strong>PaymentConnectorConfigurationSearchResponse</strong>
* <strong>PaymentConnectorConfigurationUpdate</strong>
* <strong>PaymentConnectorFeature</strong>
* <strong>PaymentConnectorListResponse</strong>
* <strong>PaymentConnectorSearchResponse</strong>
* <strong>PaymentContract</strong>
* <strong>PaymentContractState</strong>
* <strong>PaymentContractType</strong>
* <strong>PaymentInformationHash</strong>
* <strong>PaymentInformationHashType</strong>
* <strong>PaymentLink</strong>
* <strong>PaymentLinkActive</strong>
* <strong>PaymentLinkAddressHandlingMode</strong>
* <strong>PaymentLinkCreate</strong>
* <strong>PaymentLinkListResponse</strong>
* <strong>PaymentLinkProtectionMode</strong>
* <strong>PaymentLinkSearchResponse</strong>
* <strong>PaymentLinkUpdate</strong>
* <strong>PaymentMethod</strong>
* <strong>PaymentMethodBrand</strong>
* <strong>PaymentMethodBrandListResponse</strong>
* <strong>PaymentMethodBrandSearchResponse</strong>
* <strong>PaymentMethodConfiguration</strong>
* <strong>PaymentMethodConfigurationActive</strong>
* <strong>PaymentMethodConfigurationCreate</strong>
* <strong>PaymentMethodConfigurationListResponse</strong>
* <strong>PaymentMethodConfigurationSearchResponse</strong>
* <strong>PaymentMethodConfigurationUpdate</strong>
* <strong>PaymentMethodListResponse</strong>
* <strong>PaymentMethodSearchResponse</strong>
* <strong>PaymentPrimaryRiskTaker</strong>
* <strong>PaymentProcessor</strong>
* <strong>PaymentProcessorConfiguration</strong>
* <strong>PaymentProcessorConfigurationActive</strong>
* <strong>PaymentProcessorConfigurationCreate</strong>
* <strong>PaymentProcessorConfigurationListResponse</strong>
* <strong>PaymentProcessorConfigurationSearchResponse</strong>
* <strong>PaymentProcessorListResponse</strong>
* <strong>PaymentProcessorSearchResponse</strong>
* <strong>PaymentTerminal</strong>
* <strong>PaymentTerminalAddress</strong>
* <strong>PaymentTerminalConfiguration</strong>
* <strong>PaymentTerminalConfigurationState</strong>
* <strong>PaymentTerminalConfigurationVersion</strong>
* <strong>PaymentTerminalConfigurationVersionState</strong>
* <strong>PaymentTerminalCreate</strong>
* <strong>PaymentTerminalDccTransactionSum</strong>
* <strong>PaymentTerminalLocation</strong>
* <strong>PaymentTerminalLocationState</strong>
* <strong>PaymentTerminalLocationVersion</strong>
* <strong>PaymentTerminalLocationVersionState</strong>
* <strong>PaymentTerminalPreparing</strong>
* <strong>PaymentTerminalReceiptType</strong>
* <strong>PaymentTerminalState</strong>
* <strong>PaymentTerminalTransactionSum</strong>
* <strong>PaymentTerminalTransactionSummary</strong>
* <strong>PaymentTerminalTransactionSummaryReference</strong>
* <strong>PaymentTerminalType</strong>
* <strong>PaymentTerminalUpdate</strong>
* <strong>Permission</strong>
* <strong>PermissionListResponse</strong>
* <strong>PermissionSearchResponse</strong>
* <strong>PersistableCurrencyAmount</strong>
* <strong>PersistableCurrencyAmountUpdate</strong>
* <strong>ProductComponentGroupListResponse</strong>
* <strong>ProductComponentGroupSearchResponse</strong>
* <strong>ProductComponentListResponse</strong>
* <strong>ProductComponentSearchResponse</strong>
* <strong>ProductFeeType</strong>
* <strong>ProductListResponse</strong>
* <strong>ProductMeteredFee</strong>
* <strong>ProductMeteredFeeListResponse</strong>
* <strong>ProductMeteredFeeSearchResponse</strong>
* <strong>ProductMeteredFeeTierListResponse</strong>
* <strong>ProductMeteredFeeTierSearchResponse</strong>
* <strong>ProductMeteredFeeUpdate</strong>
* <strong>ProductMeteredTierFee</strong>
* <strong>ProductMeteredTierFeeUpdate</strong>
* <strong>ProductMeteredTierPricing</strong>
* <strong>ProductPeriodFee</strong>
* <strong>ProductPeriodFeeListResponse</strong>
* <strong>ProductPeriodFeeSearchResponse</strong>
* <strong>ProductPeriodFeeUpdate</strong>
* <strong>ProductRetirementListResponse</strong>
* <strong>ProductRetirementSearchResponse</strong>
* <strong>ProductSearchResponse</strong>
* <strong>ProductSetupFee</strong>
* <strong>ProductSetupFeeListResponse</strong>
* <strong>ProductSetupFeeSearchResponse</strong>
* <strong>ProductSetupFeeUpdate</strong>
* <strong>ProductVersionListResponse</strong>
* <strong>ProductVersionRetirementListResponse</strong>
* <strong>ProductVersionRetirementSearchResponse</strong>
* <strong>ProductVersionSearchResponse</strong>
* <strong>RecurringIndicator</strong>
* <strong>Refund</strong>
* <strong>RefundBankTransaction</strong>
* <strong>RefundBankTransactionListResponse</strong>
* <strong>RefundBankTransactionSearchResponse</strong>
* <strong>RefundComment</strong>
* <strong>RefundCommentActive</strong>
* <strong>RefundCommentCreate</strong>
* <strong>RefundCommentListResponse</strong>
* <strong>RefundCommentSearchResponse</strong>
* <strong>RefundCreate</strong>
* <strong>RefundListResponse</strong>
* <strong>RefundRecoveryBankTransaction</strong>
* <strong>RefundRecoveryBankTransactionListResponse</strong>
* <strong>RefundRecoveryBankTransactionSearchResponse</strong>
* <strong>RefundSearchResponse</strong>
* <strong>RefundState</strong>
* <strong>RefundType</strong>
* <strong>RenderedDocument</strong>
* <strong>RenderedTerminalReceipt</strong>
* <strong>RenderedTerminalReceiptListResponse</strong>
* <strong>RenderedTerminalTransactionSummary</strong>
* <strong>RestAddressFormat</strong>
* <strong>RestAddressFormatField</strong>
* <strong>RestApiBulkOperationResult</strong>
* <strong>RestApiErrorResponse</strong>
* <strong>RestApplicationUserMacKey</strong>
* <strong>RestApplicationUserMacKeyCreated</strong>
* <strong>RestCountry</strong>
* <strong>RestCountryState</strong>
* <strong>RestCurrency</strong>
* <strong>RestCustomerEmailAddress</strong>
* <strong>RestLanguage</strong>
* <strong>ResultPortionModel</strong>
* <strong>Role</strong>
* <strong>RoleCreate</strong>
* <strong>RoleListResponse</strong>
* <strong>RoleSearchResponse</strong>
* <strong>RoleState</strong>
* <strong>RoleUpdate</strong>
* <strong>SalesChannel</strong>
* <strong>SalesChannelListResponse</strong>
* <strong>SalesChannelSearchResponse</strong>
* <strong>Scope</strong>
* <strong>ScopeSingleSignOnProvider</strong>
* <strong>SingleSignOnUser</strong>
* <strong>SingleSignOnUserCreate</strong>
* <strong>SingleSignOnUserListResponse</strong>
* <strong>SingleSignOnUserSearchResponse</strong>
* <strong>SingleSignOnUserUpdate</strong>
* <strong>SortingOrder</strong>
* <strong>Space</strong>
* <strong>SpaceAddress</strong>
* <strong>SpaceAddressCreate</strong>
* <strong>SpaceCreate</strong>
* <strong>SpaceListResponse</strong>
* <strong>SpaceSearchResponse</strong>
* <strong>SpaceUpdate</strong>
* <strong>SpaceView</strong>
* <strong>StaticValue</strong>
* <strong>StaticValueListResponse</strong>
* <strong>StaticValueSearchResponse</strong>
* <strong>SubmittedAnalyticsQueryExecution</strong>
* <strong>Subscriber</strong>
* <strong>SubscriberActive</strong>
* <strong>SubscriberCreate</strong>
* <strong>SubscriberListResponse</strong>
* <strong>SubscriberSearchResponse</strong>
* <strong>SubscriberUpdate</strong>
* <strong>Subscription</strong>
* <strong>SubscriptionAffiliate</strong>
* <strong>SubscriptionAffiliateCreate</strong>
* <strong>SubscriptionAffiliateDeleted</strong>
* <strong>SubscriptionAffiliateDeleting</strong>
* <strong>SubscriptionAffiliateInactive</strong>
* <strong>SubscriptionAffiliateListResponse</strong>
* <strong>SubscriptionAffiliateSearchResponse</strong>
* <strong>SubscriptionAffiliateUpdate</strong>
* <strong>SubscriptionCharge</strong>
* <strong>SubscriptionChargeCreate</strong>
* <strong>SubscriptionChargeListResponse</strong>
* <strong>SubscriptionChargeProcessingType</strong>
* <strong>SubscriptionChargeSearchResponse</strong>
* <strong>SubscriptionChargeState</strong>
* <strong>SubscriptionChargeType</strong>
* <strong>SubscriptionComponentConfiguration</strong>
* <strong>SubscriptionComponentReferenceConfiguration</strong>
* <strong>SubscriptionCreateRequest</strong>
* <strong>SubscriptionInitializeSubscriberPresentRequest</strong>
* <strong>SubscriptionLedgerEntry</strong>
* <strong>SubscriptionLedgerEntryCreate</strong>
* <strong>SubscriptionLedgerEntryListResponse</strong>
* <strong>SubscriptionLedgerEntrySearchResponse</strong>
* <strong>SubscriptionLedgerEntryState</strong>
* <strong>SubscriptionListResponse</strong>
* <strong>SubscriptionMetric</strong>
* <strong>SubscriptionMetricActive</strong>
* <strong>SubscriptionMetricCreate</strong>
* <strong>SubscriptionMetricType</strong>
* <strong>SubscriptionMetricUpdate</strong>
* <strong>SubscriptionMetricUsageReport</strong>
* <strong>SubscriptionMetricUsageReportCreate</strong>
* <strong>SubscriptionPending</strong>
* <strong>SubscriptionPeriodBill</strong>
* <strong>SubscriptionPeriodBillListResponse</strong>
* <strong>SubscriptionPeriodBillSearchResponse</strong>
* <strong>SubscriptionPeriodBillState</strong>
* <strong>SubscriptionProduct</strong>
* <strong>SubscriptionProductActive</strong>
* <strong>SubscriptionProductComponent</strong>
* <strong>SubscriptionProductComponentGroup</strong>
* <strong>SubscriptionProductComponentGroupUpdate</strong>
* <strong>SubscriptionProductComponentReference</strong>
* <strong>SubscriptionProductComponentReferenceState</strong>
* <strong>SubscriptionProductComponentUpdate</strong>
* <strong>SubscriptionProductCreate</strong>
* <strong>SubscriptionProductRetirement</strong>
* <strong>SubscriptionProductRetirementRequest</strong>
* <strong>SubscriptionProductState</strong>
* <strong>SubscriptionProductVersion</strong>
* <strong>SubscriptionProductVersionPending</strong>
* <strong>SubscriptionProductVersionRetirement</strong>
* <strong>SubscriptionProductVersionRetirementRequest</strong>
* <strong>SubscriptionProductVersionState</strong>
* <strong>SubscriptionSearchResponse</strong>
* <strong>SubscriptionState</strong>
* <strong>SubscriptionSuspension</strong>
* <strong>SubscriptionSuspensionAction</strong>
* <strong>SubscriptionSuspensionReason</strong>
* <strong>SubscriptionSuspensionState</strong>
* <strong>SubscriptionUpdate</strong>
* <strong>SubscriptionUpdateRequest</strong>
* <strong>SubscriptionVersion</strong>
* <strong>SubscriptionVersionListResponse</strong>
* <strong>SubscriptionVersionSearchResponse</strong>
* <strong>SubscriptionVersionState</strong>
* <strong>SuspensionCreationRequest</strong>
* <strong>SuspensionListResponse</strong>
* <strong>SuspensionSearchResponse</strong>
* <strong>Tax</strong>
* <strong>TaxCalculation</strong>
* <strong>TaxClass</strong>
* <strong>TaxCreate</strong>
* <strong>TenantDatabase</strong>
* <strong>TerminalListResponse</strong>
* <strong>TerminalReceiptFormat</strong>
* <strong>TerminalSearchResponse</strong>
* <strong>TerminalTransactionSummaryListResponse</strong>
* <strong>TerminalTransactionSummarySearchResponse</strong>
* <strong>Token</strong>
* <strong>TokenCreate</strong>
* <strong>TokenListResponse</strong>
* <strong>TokenSearchResponse</strong>
* <strong>TokenUpdate</strong>
* <strong>TokenVersion</strong>
* <strong>TokenVersionListResponse</strong>
* <strong>TokenVersionRetryStrategy</strong>
* <strong>TokenVersionSearchResponse</strong>
* <strong>TokenVersionState</strong>
* <strong>TokenVersionType</strong>
* <strong>TokenizationMode</strong>
* <strong>TokenizedCardData</strong>
* <strong>TokenizedCardDataCreate</strong>
* <strong>TokenizedCardRequest</strong>
* <strong>Transaction</strong>
* <strong>TransactionClientPlatformInformation</strong>
* <strong>TransactionComment</strong>
* <strong>TransactionCommentActive</strong>
* <strong>TransactionCommentCreate</strong>
* <strong>TransactionCommentListResponse</strong>
* <strong>TransactionCommentSearchResponse</strong>
* <strong>TransactionCompletion</strong>
* <strong>TransactionCompletionBehavior</strong>
* <strong>TransactionCompletionDetails</strong>
* <strong>TransactionCompletionMode</strong>
* <strong>TransactionCompletionState</strong>
* <strong>TransactionCreate</strong>
* <strong>TransactionEnvironmentSelectionStrategy</strong>
* <strong>TransactionGroup</strong>
* <strong>TransactionGroupState</strong>
* <strong>TransactionInvoice</strong>
* <strong>TransactionInvoiceComment</strong>
* <strong>TransactionInvoiceCommentActive</strong>
* <strong>TransactionInvoiceCommentCreate</strong>
* <strong>TransactionInvoiceReplacement</strong>
* <strong>TransactionInvoiceState</strong>
* <strong>TransactionLineItemVersion</strong>
* <strong>TransactionLineItemVersionCreate</strong>
* <strong>TransactionLineItemVersionState</strong>
* <strong>TransactionListResponse</strong>
* <strong>TransactionPending</strong>
* <strong>TransactionSearchResponse</strong>
* <strong>TransactionState</strong>
* <strong>TransactionUserInterfaceType</strong>
* <strong>TransactionVoid</strong>
* <strong>TransactionVoidListResponse</strong>
* <strong>TransactionVoidMode</strong>
* <strong>TransactionVoidSearchResponse</strong>
* <strong>TransactionVoidState</strong>
* <strong>TwoFactorAuthenticationType</strong>
* <strong>User</strong>
* <strong>UserAccountRole</strong>
* <strong>UserAccountRoleListResponse</strong>
* <strong>UserSpaceRole</strong>
* <strong>UserSpaceRoleListResponse</strong>
* <strong>UserType</strong>
* <strong>WalletType</strong>
* <strong>WebAppConfirmationResponse</strong>
* <strong>WebhookIdentity</strong>
* <strong>WebhookListener</strong>
* <strong>WebhookListenerCreate</strong>
* <strong>WebhookListenerEntity</strong>
* <strong>WebhookListenerListResponse</strong>
* <strong>WebhookListenerSearchResponse</strong>
* <strong>WebhookListenerUpdate</strong>
* <strong>WebhookURLListResponse</strong>
* <strong>WebhookURLSearchResponse</strong>
* <strong>WebhookUrl</strong>
* <strong>WebhookUrlCreate</strong>
* <strong>WebhookUrlUpdate</strong>

</details>

## Error Codes

When working with webhooks, the `WalleeSdkException` may throw error codes to help with debugging.

### Error Code Categories

| **Exception**              | **Description**                                                                       |
|----------------------------|---------------------------------------------------------------------------------------|
| **ApiExceptionErrorCodes** | Lists the possible HTTP error codes an `ApiException` can generate                    |
| **SdkExceptionErrorCodes** | Lists the possible error codes a `WalleeSdkException` can generate |

### Usage Example
```python
try:
    # SDK operation
except ApiException as ex:
    if ApiExceptionErrorCodes.CONFLICT.matches(ex):
        # Handle Conflict
    else:
        # Other handling
```

## Author
- Wallee Ecosystem Team<br><br>

*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*
<br>Generator version: 7.13.0

## License

Please see the [license file](https://github.com/wallee-payment/python-sdk/blob/master/LICENSE) for more information.
