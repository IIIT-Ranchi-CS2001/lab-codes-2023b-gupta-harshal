def my_zip(name,id,points,struct):
    if struct:
        if(len(name)==len(id)==len(points)):
            return zip(name,id,points)
        else:
            return []
    else:
        min_len = min(len(name), len(id), len(points))
        return zip(name[:min_len], id[:min_len], points[:min_len])
customer_names=["Aryan","Utkarsh","Aakristh","Sattu"]
customer_ids=["1","2","3","4"]
points=["5","8","9","4"]
ans=my_zip(customer_names,customer_ids,points,struct=True)
for entry in ans:
    print(entry)