# Use the official Node.js image as the base image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json to the container
COPY package.json package-lock.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the frontend files into the container
COPY . .

# Expose the port your app runs on (adjust if necessary)
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
