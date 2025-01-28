<template>
  <div id="app">
    <h1>Ankara 7 Günlük Hava Durumu</h1>
    <div v-if="loading">Yükleniyor...</div>
    <div v-else-if="error">Hata: {{ error }}</div>
    <div v-else>
      <ul>
        <li v-for="(day, index) in weatherData" :key="index">
          <p><strong>Gün:</strong> {{ getDayName(day.dt) }}</p>
          <p><strong>Sıcaklık:</strong> {{ day.temp.day }}°C</p>
          <p><strong>Hava Durumu:</strong> {{ day.weather[0].description }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "App",
  setup() {
    const weatherData = ref([]);
    const loading = ref(true);
    const error = ref(null);

    const fetchWeatherData = async () => {
      try {
        const response = await fetch(
          'https://api.openweathermap.org/data/2.5/onecall?lat=39.9208&lon=32.8541&exclude=current,minutely,hourly,alerts&units=metric&lang=tr&appid=6f46b30feb064919ba8ebd742bbcff7c'
        );

        if (!response.ok) {
          throw new Error("Veri alınamadı: " + response.statusText);
        }

        const data = await response.json();
        weatherData.value = data.daily;
      } catch (err) {
        error.value = err.message;
      } finally {
        loading.value = false;
      }
    };


    const getDayName = (timestamp) => {
      const date = new Date(timestamp * 1000);
      const days = ["Pazar", "Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi"];
      return days[date.getDay()];
    };

    onMounted(() => {
      fetchWeatherData();
    });

    return {
      weatherData,
      loading,
      error,
      getDayName,
    };
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  margin: 20px;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
