# Food Recommendation System API

This project provides a recommendation system API trained on the food.com dataset. It uses FastAPI to serve the recommendations and Docker for containerization.

## Table of Contents

- Features
- Requirements
- Installation
- Usage
- API Endpoints
- Docker
- Backend Developer
- Flutter App Developer
- Contributing
- License

## Features

- Recommends recipes based on favorite cuisines, ingredients, and dishes.
- Configurable number of recommended recipes (default is 10).
- Built with FastAPI for a high-performance API.
- Dockerized for easy deployment.

## Requirements

- Python 3.8+
- FastAPI
- scikit-learn
- pandas
- Docker

## Installation

1. Pull the Docker image:
   ```sh
   bash
   docker pull abdelrahmanmenisy2002/food_recommendation_sys
   

3. Run the Docker container:
   ```sh
   bash
   docker run -d -p 8000:8000 abdelrahmanmenisy2002/food_recommendation_sys
   

## Usage

### Running the API

1. The API will be accessible at
   ```sh
   `http://127.0.0.1:8000`.

## API Endpoints

### `GET /recommendations`

#### Parameters:
- `favorite_cuisines` (List[str]): A list of favorite cuisines.
- `favorite_ingredients` (List[str]): A list of favorite ingredients.
- `favorite_dishes` (List[str]): A list of favorite dishes.
- `num_recommendations` (int, optional): Number of recipes to recommend (default is 10).

#### Example Request:
http  
```sh
GET /recommendations?favorite_cuisines=Italian,Chinese&favorite_ingredients=chicken,tomato&favorite_dishes=pizza,pasta&num_recommendations=5
```

#### Example Response:
```sh
json
{
  "recommendations": [
    "Recipe 1",
    "Recipe 2",
    "Recipe 3",
    "Recipe 4",
    "Recipe 5"
  ]
}
```

## Docker

### Building the Docker Image

1. Build the Docker image:
```sh
   bash
   docker build -t food_recommendation_sys .
   ```

2. Run the Docker container:
```sh
   bash
   docker run -d -p 8000:8000 food_recommendation_sys
   ```

### Pulling from Docker Hub

1. Pull the Docker image:
```sh
   bash
   docker pull abdelrahmanmenisy2002/food_recommendation_sys
   ```

### Running the Docker Container

1. Run the Docker container:
```sh
   bash
   docker run -d -p 8000:8000 abdelrahmanmenisy2002/food_recommendation_sys
   ```

### Pushing to Docker Hub

1. Tag the Docker image:
```sh
   bash
   docker tag food_recommendation_sys abdelrahmanmenisy2002/food_recommendation_sys
   ```

2. Push the Docker image to Docker Hub:
```sh
   bash
   docker push abdelrahmanmenisy2002/food_recommendation_sys
   ```

## Backend Developer

This project is used by the backend developer:
[Omar Saeed](https://github.com/Omarsa2002)

## Flutter App Developer

This project is used by the Flutter app developer:
[Mohamed Ghaly](https://github.com/Mohamed15Ghaly)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
