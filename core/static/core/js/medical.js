document.addEventListener('DOMContentLoaded', () => {
    const locationError = document.getElementById('locationError');
    const hospitalsList = document.getElementById('hospitals-list');
    const pharmaciesList = document.getElementById('pharmacies-list');
    
    const showMedicalResults = (type, results) => {
        const container = type === 'hospital' ? hospitalsList : pharmaciesList;
        container.innerHTML = results.map(result => `
            <div class="medical-item">
                <div class="medical-name">${result.name}</div>
                <div class="medical-distance">${result.distance} km</div>
                <div class="medical-address">${result.address}</div>
                ${result.rating ? `<div class="medical-rating">⭐ ${result.rating}</div>` : ''}
            </div>
        `).join('');
    };

    const getLocation = () => {
        return new Promise((resolve, reject) => {
            if (!navigator.geolocation) {
                reject('Geolocation not supported');
                return;
            }
            
            navigator.geolocation.getCurrentPosition(
                position => resolve(position.coords),
                error => reject('Location permission denied')
            );
        });
    };

    const loadMedicalData = async () => {
        try {
            const coords = await getLocation();
            
            const response = await fetch('/get-medical/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': '{{ csrf_token }}'
                },
                body: new URLSearchParams({
                    'lat': coords.latitude,
                    'lng': coords.longitude
                })
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                showMedicalResults('hospital', data.results.hospitals);
                showMedicalResults('pharmacy', data.results.pharmacies);
            } else {
                throw new Error(data.message);
            }
            
        } catch (error) {
            locationError.textContent = `Error: ${error.message}. Showing default listings.`;
            // Default listings already visible from Django template
        }
    };

    // Automatically load on homepage visit
    loadMedicalData();
});