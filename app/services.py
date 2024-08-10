from sklearn.cluster import KMeans
from .models import Dish

def clusterize_data():
    dishes = Dish.objects.all()
    
    data = []
    for dish in dishes:
        data.append([dish.calory, dish.time])
    
    k = 5  # Количество кластеров (можно изменить)
    kmeans = KMeans(n_clusters=k)

    clusters = kmeans.fit_predict(data)
    
    # Убираем присваивание атрибута cluster объектам Dish
