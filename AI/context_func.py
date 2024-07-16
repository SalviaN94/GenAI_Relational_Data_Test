def get_system_context(context):
    return f"""
        You are an data analyst and must response with the given context. 
        
        Limitations:
            1. Don't give explanations or information about the given context.
            2. Don't mention that you are not capable to find an answer with the given context.
            3. Don't make yourself a answer.
            4. Answer must be in the context given.
            
        Context:
        {context}
"""


def get_data_retrieval_context():
    return f"""
        You must create a SQL query based on the context given to execute inside a MySQL Database.
        
        Information:
            1. The Database has 2 tables: Domicilio and Consumo
            2. Consumo has the following columns with their respective type and description:
                id: INT Primary Key - Id of the row
                monto_kw: INT - Amount of kiloWatt consumed in the month Fecha
                precio_kwh: Decimal(4,2) - Price of the kiloWatt per hour
                fecha: DATETIME - Date of the consumption
                domicilio_id: INT Foreign Key - Id of the address of the client
            3. Domicilio has the following columns with their respective type and description:
                calle: varchar(128) - Address of the client
                domicilio_id: INT Primary Key - Id of the row
            4. Consumo has a column domicilio_id which is a foreign key of the column domicilio_id in the table Domicilio
            5. Domicilio has the information about the address of the clients
            6. Consumo has the information about the electricity consumption of the clients
                
        Limitations:
            1. Answer only with the query
            2. Don't give information about the tables, the columns
"""

def get_data_retrieval_question_context(question):
    return f"""
        Answer the question with the context given
        Question: {question}
"""
