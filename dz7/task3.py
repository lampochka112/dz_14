import json
import csv

# Декоратор для формата JSON
def json_report(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result, indent=4)
    return wrapper

# Декоратор для формата CSV
def csv_report(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        output = []
        output.append(list(result[0].keys()))
        for row in result:
            output.append(list(row.values()))
        csv_output = "\n".join([",".join(map(str, row)) for row in output])
        return csv_output
    return wrapper

def pdf_report(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        pdf_output = "\n".join([f"{key}: {value}" for key, value in result.items()])
        return pdf_output
    return wrapper

def generate_report(organization_type):
    report_data = {
        "revenue": 1000000,
        "expenses": 500000,
        "profit": 500000
    }

    if organization_type == 'government':
        @json_report
        def report():
            return report_data
    elif organization_type == 'business':
        @csv_report
        def report():
            return [report_data]
    elif organization_type == 'nonprofit':
        @pdf_report
        def report():
            return report_data
    else:
        return "Тип организации не поддерживается."

    return report()

organization_type = input("Введите тип организации (government, business, nonprofit): ").strip().lower()

print("\nОтчет:")
print(generate_report(organization_type))