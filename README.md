# FastAPI Starter

This is a starter project for a FastAPI application.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/jleeapp/fastapi-starter.git
   ```

2. Create a virtual environment and activate it:

   ```sh
   cd fastapi-starter
   python3 -m venv venv
   ```

   ### venv activation

   #### Mac & Linux

   ```sh
   source venv/bin/activate
   ```

   #### Windows 

   To activate your venv on Windows, you need to run a script that gets installed by venv.

   ##### In cmd.exe

   ```sh
   venv\Scripts\activate.bat
   ```

   ##### In PowerShell

   ```sh
   venv\Scripts\Activate.ps1
   ```


3. Install the requirements:

   ```sh
   pip3 install -r requirements.txt
   ```

## Running the Application

To run the application, use the following command:

```sh
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`.


## Test

```sh
pytest
```