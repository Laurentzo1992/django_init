let currentPatientId; // Variable pour stocker l'identifiant du patient actuel

// Ajoutez un gestionnaire d'événements click pour les boutons de modification
document.querySelector('#data-table').addEventListener('click', function (event) {
    if (event.target && event.target.id === 'modified') {
        // Récupérez les données du patient de la ligne du tableau
        const row = event.target.closest('tr');
        const currentPatientId  = row.querySelector('td:nth-child(1)').textContent;
       
        const patientLastName = row.querySelector('td:nth-child(2)').textContent;
        const patientFirstName = row.querySelector('td:nth-child(3)').textContent;
        const patientPhone = row.querySelector('td:nth-child(4)').textContent;
        const patientpassword = row.querySelector('td:nth-child(5)').textContent;

        //Remplissez le formulaire de modification avec les données actuelles du patient
        document.querySelector('#last_name').value = patientLastName;
        document.querySelector('#first_name').value = patientFirstName;
        document.querySelector('#phone').value = patientPhone;
        document.querySelector('#password').value = patientpassword;

        // Affichez le formulaire de modification
        //document.querySelector('#edit-form').style.display = 'block';
    }
});

// Ajoutez un gestionnaire d'événements submit pour le formulaire de modification
document.querySelector('#api_request').addEventListener('submit', function (event) {
    event.preventDefault();

    // Récupérez les données du formulaire
    const newLastName = document.querySelector('#last_name').value;
    const newFirstName = document.querySelector('#first_name').value;
    const newPhone = document.querySelector('#phone').value;
    const patientpassword = document.querySelector('#password').value;

    // Créez un objet avec les nouvelles données du patient
    const updatedPatient = {
        last_name:  newLastName,
        first_name: newFirstName,
        phone: newPhone,
        password: patientpassword

    };

    // Envoyez une requête PUT ou PATCH à votre API pour mettre à jour les données du patient
    const apiUrl = `http://127.0.0.1:8000/api/patient/${currentPatientId}/`;
    fetch(apiUrl, {
        method: 'PUT', // Utilisez 'PUT' ou 'PATCH' en fonction de votre API
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedPatient),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erreur HTTP: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log('Données mises à jour:', data);

        // Mettez à jour la ligne du tableau avec les nouvelles données
        const row = document.querySelector(`#data-table tr td:nth-child(1):contains("${patientId}")`).closest('tr');
        row.querySelector('td:nth-child(1)').textContent = data.last_name;
        row.querySelector('td:nth-child(2)').textContent = data.first_name;
        row.querySelector('td:nth-child(3)').textContent = data.phone;
        row.querySelector('td:nth-child(4)').textContent = data.password;

        // Cachez le formulaire de modification
        //document.querySelector('#edit-form').style.display = 'none';
    })
    .catch(error => {
        console.error('Erreur lors de la mise à jour des données:', error);
    });
});
