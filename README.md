# Dog Website and Pet API

## Website

Built with Next, Shad UI, Tailwind and React Query. To start the dev server, run:

```
cd frontend
npm install
npm run dev
```

and navigate to `http://localhost:3000`

## API

Built with FastAPI, Poetry, and a Sqlite database. To start the server, run:

```
cd backend
poetry install
poetry run start
```

## API Endpoints

The server will be running at `http://localhost:8000`

### Create a Pet

```http
PUT /pets
```

Body

```json
{
  "name": string,
  "breed": string,
  "type": string,
  "image": string,
  "ranking": number,
}
```

### Get all pets of a type

```http
GET /pets?type={type}
```

### Get a pet by name

```http
GET /pets/{name}
```

### Delete a pet by name

```http
DELETE /pets/{name}
```

### Delete all pets of a type

```http
DELETE /pets?type={type}
```
