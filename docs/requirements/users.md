# System Users

## Customer
- Browse products
- Place orders
- Track orders
- Request returns
- Request customization
- Manage personal information

## Staff
- Manage assigned business operations
- View customers
- Manage orders
- Update delivery information

## Owner
- Full system access
- Manage products
- Manage staff
- Manage orders
- Manage customers and leads
- View analytics
- Manage business settings

## User Information

Every system user has:

- Unique ID
- Email address
- Password
- First name
- Last name
- Role
- Account active/inactive status
- Date joined
- Last login

### Authentication

- Users log in using their email address and password.
- Each user has a role: Customer, Staff, or Owner.
- Access to system functionality is controlled according to the user's role.

## Separation of User and Customer

The User entity manages authentication, authorization and system access.

The Customer entity manages business-specific information about a customer.

Not every User is a Customer.

A Customer is associated with one User account.

## Customer Information

A Customer stores business-specific information associated with a User account.

Initial customer information:

- Phone number
- Delivery address
- City
- Business notes
- Created date
- Updated date

Customer addresses should be designed separately so that a customer can have multiple addresses.

## Customer Address

A Customer can have multiple delivery addresses.

Each address contains:

- Label
- Recipient name
- Phone number
- Address line 1
- Address line 2
- City
- District
- Postal code
- Default address status
- Created date
- Updated date

An address belongs to one Customer.

An order must preserve the delivery address that was used when the order was placed.

## Roles and Permissions

The system uses three primary user roles:

### Customer
Can manage their own account, browse products, place orders, track orders, and submit eligible requests.

### Staff
Can perform assigned business operations such as managing products, orders, customers, leads, and delivery information.

### Owner
Has full business access, including staff management, analytics, and business configuration.

Role-based access control will be implemented using Django's authentication and permission system.