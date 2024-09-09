<template>
    <div id="map"></div>
  </template>
  
  <script>
  import L from 'leaflet';
  
  export default {
    mounted() {
      // Create a Leaflet map
      const map = L.map('map').setView([40.7128, -74.0060], 13);
  
      // Add a tile layer
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map);
  
      // Access the routes data from the router (assuming passed as props)
      const routes = this.$route.query.routes // Or this.$route.params.routes depending on your routing setup
  
      if (routes) {
        // Parse the routes data (assuming it's a JSON string)
        const parsedRoutes = JSON.parse(routes);
  
        // Iterate through routes and add markers and lines to the map
        parsedRoutes.forEach(route => {
          const locations = route.locations.map(location => [/* latitude, longitude */]);
  
          const routeLine = L.polyline(locations, { color: 'blue' }).addTo(map);
  
          // Add markers for each location
          locations.forEach(location => {
            L.marker(location).addTo(map);
          });
        });
      } else {
        console.error('Missing routes data in query parameters');
      }
    }
  };
  </script>