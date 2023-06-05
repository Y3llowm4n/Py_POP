from flask import Blueprint, render_template, request, flash, redirect
import pypyodbc as odbc
import pandas as pd 
import sys
from credential import username, password

views = Blueprint(__name__, "views")

@views.route("/", methods=['GET', 'POST'])
def insert_table():
    if request.method == 'POST':
        discount_code = request.form['discount_code']
        conn = None
        cursor = None  # Initialize cursor with None

# configre new connection string after renaming database
        try:
            # Connect to the Azure SQL Database
            connection_string = (
                'DRIVER={ODBC Driver 18 for SQL Server};Server=tcp:terraform-sql-server01.database.windows.net,1433;Database=terraform-sql-db01;Uid=' + username + ';Pwd=' + password + ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()

            # Check if table 'DiscountCodes' exists
            cursor.execute(
                "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'DiscountCodes'")
            table_exists = cursor.fetchone()

            if not table_exists:
                # Create the table 'DiscountCodes' if it doesn't exist
                cursor.execute("CREATE TABLE DiscountCodes (DiscCode VARCHAR(255))")
                conn.commit()
                flash("Table 'DiscountCodes' created successfully!", "info")

            # Insert the discount code into the 'DiscountCodes' table
            cursor.execute(
                "INSERT INTO DiscountCodes (DiscCode) VALUES (?)", (discount_code,))
            conn.commit()
            flash("Code successfully applied!", "info")
            return redirect(request.url)

        except Exception as e:
            return f'An error occurred: {str(e)}'

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    return render_template("index.html")
