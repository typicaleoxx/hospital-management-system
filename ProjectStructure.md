# Hospital Management System Project Outline

## 1. Accounts

### Description

Manages user authentication, role-based access, and user profile information.

### Models

- **User**

  - `username`: CharField
  - `email`: EmailField
  - `password`: CharField (encrypted)
  - `role`: CharField (choices: ['Doctor', 'Receptionist', 'Nurse', 'Pharmacist', 'Admin'])

- **Profile**
  - `user`: OneToOneField(User)
  - `phone_number`: CharField
  - `address`: TextField
  - `profile_picture`: ImageField (optional)

## 2. Patients

### Description

Manages patient data, including registration, basic information, and health records.

### Models

- **Patient**
  - `name`: CharField
  - `contact_information`: CharField
  - `dob`: DateField
  - `gender`: CharField
  - `medical_history`: TextField
  - `registration_date`: DateTimeField
  - `insurance_info`: TextField (to store insurance details)

## 3. Doctors

### Description

Handles doctor profiles, specializations, and scheduling.

### Models

- **Doctor**
  - `user`: OneToOneField(User)
  - `specialization`: CharField
  - `department`: CharField
  - `availability_schedule`: JSONField (to store weekly availability)

## 4. Appointments

### Description

Manages appointment scheduling and status.

### Models

- **Appointment**
  - `patient`: ForeignKey(Patient)
  - `doctor`: ForeignKey(Doctor)
  - `date_time`: DateTimeField
  - `status`: CharField (choices: ['Scheduled', 'Completed', 'Cancelled'])
  - `notes`: TextField (optional, for appointment-specific notes)

## 5. Medical Records

### Description

Manages electronic health records (EHR) for each patient.

### Models

- **MedicalRecord**
  - `patient`: ForeignKey(Patient)
  - `doctor`: ForeignKey(Doctor)
  - `date`: DateTimeField
  - `diagnosis`: TextField
  - `treatment`: TextField
  - `prescription`: TextField
  - `follow_up_date`: DateField (optional, for future appointments)

## 6. Billing

### Description

Handles billing and payment tracking for services.

### Models

- **Invoice**
  - `patient`: ForeignKey(Patient)
  - `doctor`: ForeignKey(Doctor, null=True)
  - `amount`: DecimalField
  - `date`: DateTimeField
  - `status`: CharField (choices: ['Paid', 'Pending', 'Overdue'])
  - `payment_method`: CharField (choices: ['Cash', 'Credit Card', 'Insurance'])

## 7. Inventory

### Description

Manages stock levels of medical supplies, equipment, and medications.

### Models

- **InventoryItem**
  - `name`: CharField
  - `quantity`: IntegerField
  - `unit_price`: DecimalField
  - `expiration_date`: DateField
  - `last_updated`: DateTimeField

## 8. Emergency Management

### Description

Manages emergency cases, patient triage, and rapid response protocols.

### Models

- **Emergency**
  - `patient`: ForeignKey(Patient)
  - `type`: CharField (e.g., 'Cardiac Arrest', 'Trauma', 'Other')
  - `timestamp`: DateTimeField
  - `severity`: CharField (choices: ['Low', 'Medium', 'High'])
  - `status`: CharField (choices: ['Treated', 'Under Observation', 'Discharged'])

## 9. Reports

### Description

Generates analytical reports on hospital operations and key metrics.

### Models

- **Report**
  - `type`: CharField (e.g., 'Appointment Report', 'Billing Report', 'Inventory Report')
  - `date_generated`: DateTimeField
  - `content`: TextField (or use JSON for structured data)

# Practical Example

## Patient Visit Workflow

1. **Patient Registration**

   - Receptionist registers patient details.
   - Patient record created.

2. **Appointment Scheduling**

   - Receptionist checks doctor's availability.
   - Appointment booked, record created.

3. **Medical Visit**

   - Doctor views patient details.
   - Medical records updated during the visit.

4. **Billing Process**

   - Invoice generated after the appointment.
   - Payment tracked.

5. **Inventory Management**

   - Stock levels updated post-appointment.

6. **Reporting and Analytics**
   - Admin generates reports for operations insights.
