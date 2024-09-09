<template>
    <div>
      <h2>Input Form</h2>
      <form @submit.prevent="submitForm">
        <label for="numVehicles">Number of Vehicles:</label>
        <input type="number" id="numVehicles" v-model="numVehicles">
  
        <label for="vehicleCapacity">Vehicle Capacity:</label>
        <input type="number" id="vehicleCapacity" v-model="vehicleCapacity">
  
        <button type="submit">Submit</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    data() {
      return {
        numVehicles: 0,
        vehicleCapacity: 0,
        // Add other input variables
      };
    },
    methods: {
      submitForm() {
        // Send input data to backend API using axios
        axios.post('http://localhost:5000/api/cvrptw', {
          numVehicles: this.numVehicles,
          vehicleCapacity: this.vehicleCapacity,
          // Add other input data
        })
        .then(response => {
            this.$router.push('/results', { routes: JSON.stringify(response.data) });
        })
        .catch(error => {
          console.error('Error submitting form:', error);
        });
      }
    }
  };
  </script>