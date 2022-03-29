import pandas as pd

def read_csv(filepath):
        
    df = pd.read_csv(filepath)
    return df

def read_csv_as_list (filepath):
    df = read_csv(filepath)

    df_sorted = df.sort_values(by="Date")
    
    return df_sorted.values.tolist()

def read_total_value(filepath):
    df = pd.read_csv(filepath)

    sum_sales = df["Sale"].sum()
    
    return sum_sales

def analyse(filepath):
    df = pd.read_csv(filepath)
    sum_sales = df.groupby(["Date"]).sum().reset_index()
    qty_sales = df.groupby(["Date"]).count().reset_index()

    min_value = sum_sales["Sale"].min() # aqui imprime valor sozinho
    row_min_value = sum_sales[ sum_sales["Sale"] == min_value ] #aqui imprime a linha 
   
    max_value = sum_sales["Sale"].max()
    row_max_value = sum_sales[sum_sales["Sale"] == max_value]

    min_qty = qty_sales["Sale"].min() 
    row_min_qty = qty_sales[qty_sales["Sale"] == min_qty]

    max_qty = qty_sales["Sale"].max()
    row_max_qty = qty_sales[qty_sales["Sale"] == max_qty]

    dict_result = {
        "min_value" : {
            "date": row_min_value["Date"].values[0],
            "value": row_min_value["Sale"].values[0]
        },
        "max_value" : {
            "date": row_max_value["Date"].values[0],
            "value": row_max_value["Sale"].values[0]
        },
        "min_qty" : {
            "date": row_min_qty["Date"].values[0],
            "value": row_min_qty["Sale"].values[0]
        },
        "max_qty" : {
            "date": row_max_qty["Date"].values[0],
            "value": row_max_qty["Sale"].values[0]
        }
    }
    
    return dict_result


