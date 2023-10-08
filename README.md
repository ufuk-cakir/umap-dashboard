
gcloud builds submit --tag gcr.io/bachelor-thesis-359123/IllustrisTNG-UMAP-Projection  --project=bachelor-thesis-359123 

gcloud run deploy --image gcr.io/bachelor-thesis-359123/IllustrisTNG-UMAP-Projection --platform managed  --project=bachelor-thesis-359123  --allow-unauthenticated


