
document.getElementById("api_request").addEventListener("submit", function(event) {
    event.preventDefault(); // Empêche le formulaire de se soumettre normalement
  
    const formData = new FormData(event.target); // Capturer les données du formulaire
    
    const data = {};
    formData.forEach((value, key) => {
      data[key] = value;
    });
  
    //const apiUrl = 'https://exemple.com/api'; // Remplacez par l'URL de l'API
    const apiUrl_post= 'http://127.0.0.1:8000/api/patient/';
  
    const requestOptions = {
      method: 'POST', // Ou 'PUT' ou 'DELETE' en fonction de votre cas
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    };
  
    fetch(apiUrl_post, requestOptions)
      .then(response => response.json())
      .then(data => {
        console.log('Réponse de l\'API :', data);
        alert("Enregistrement effectué")

      // Réinitialisez le formulaire après la soumission réussie
      event.target.reset();
      //document.querySelector('#api_request').style.display = 'none';
        
      })
      .catch(error => {
        alert("erreur ")
        console.error('Erreur lors de la requête :', error);
        // Gérez les erreurs
      });
  });
  