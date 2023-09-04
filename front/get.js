                // Variables pour la pagination
let currentPage = 1;
const itemsPerPage = 10; // Nombre d'éléments par page

// Fonction pour charger les données paginées
function loadPaginatedData(pageNumber) {
    const apiUrl = `http://127.0.0.1:8000/api/patient/?page=${pageNumber}&page_size=${itemsPerPage}`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erreur HTTP: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Données de l\'API:', data);

            const tbody = document.querySelector('#data-table tbody');
            tbody.innerHTML = ''; // Effacer le contenu précédent du tableau

            data.results.forEach(patient => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${patient.id}</td>
                    <td>${patient.phone}</td>
                    <td>${patient.first_name}</td>
                    <td>${patient.last_name}</td>
                    <td>${patient.password}</td>
                    <td>
                        <button class="btn btn-warning" id="modified">
                        <i class="fa-solid fa-pen"></i>
                        </button>
                        <button class="btn btn-danger" id="delete">
                        <i class="fa-solid fa-trash"></i>
                        </button>
                    </td>
                `;
                tbody.appendChild(row);
            });

            // Mettre à jour le numéro de page actuel
            currentPage = pageNumber;

        })
        .catch(error => {
            console.error('Erreur lors de l\'appel à l\'API:', error);
        });
}

// Au chargement initial de la page, chargez la première page de données
loadPaginatedData(currentPage);
console.log("page" + " " + currentPage)

// Lorsque l'utilisateur clique sur "Page suivante"
document.querySelector('#nextPageButton').addEventListener('click', () => {
    loadPaginatedData(currentPage + 1);
});

// Lorsque l'utilisateur clique sur "Page précédente"
document.querySelector('#previousPageButton').addEventListener('click', () => {
    if (currentPage > 1) {
        loadPaginatedData(currentPage - 1);
    }
});


