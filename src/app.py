from fastapi import FastAPI


app = FastAPI(
    title="Supply chain CRM",
    description="CRM for managing operations on tanks by users",
    version="0.0.1",
    contact={
        "name": "Andrey K.",
        "email": "andreywork@example.com",
    },
    license_info={
        "name": "MIT",
    },
)

