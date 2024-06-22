// Function to fetch data from the web service
async function fetchDataAndUpdate() {
  try {
    const response = await fetch("http://10.0.10.240:5000"); // Replace with your web service URL
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    console.log(data.message);
    document.getElementById("data-container").innerText = JSON.stringify(
      data.message,
    );
  } catch (error) {
    console.error("There has been a problem with your fetch operation:", error);
    document.getElementById("data-container").innerText = "Failed to load data";
  }
}

// Initial fetch when the page loads
fetchDataAndUpdate();

// Set up the interval to fetch data every 10 seconds (10000 milliseconds)
setInterval(fetchDataAndUpdate, 10000);
