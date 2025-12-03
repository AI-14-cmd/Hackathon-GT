// InsightX - Frontend JavaScript

let selectedFile = null;

// DOM Elements
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const fileInfo = document.getElementById('fileInfo');
const fileName = document.getElementById('fileName');
const fileSize = document.getElementById('fileSize');
const removeFileBtn = document.getElementById('removeFile');
const generateBtn = document.getElementById('generateBtn');
const sampleBtn = document.getElementById('sampleBtn');
const statusMessage = document.getElementById('statusMessage');
const progressBar = document.getElementById('progressBar');
const progressFill = document.getElementById('progressFill');
const progressText = document.getElementById('progressText');

// File size formatter
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
}

// Show status message
function showStatus(message, type = 'info') {
    statusMessage.className = `status-${type}`;
    statusMessage.innerHTML = `
        <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            ${type === 'success' ?
            '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>' :
            type === 'error' ?
                '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>' :
                '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>'
        }
        </svg>
        <span>${message}</span>
    `;
    statusMessage.classList.remove('hidden');
}

// Hide status message
function hideStatus() {
    statusMessage.classList.add('hidden');
}

// Show progress bar
function showProgress(percent = 0) {
    progressBar.classList.remove('hidden');
    progressFill.style.width = `${percent}%`;
    progressText.textContent = `${percent}%`;
}

// Hide progress bar
function hideProgress() {
    progressBar.classList.add('hidden');
    progressFill.style.width = '0%';
    progressText.textContent = '0%';
}

// Handle file selection
function handleFileSelect(file) {
    if (!file) return;

    if (!file.name.endsWith('.csv')) {
        showStatus('Please select a CSV file', 'error');
        return;
    }

    selectedFile = file;
    fileName.textContent = file.name;
    fileSize.textContent = formatFileSize(file.size);
    fileInfo.classList.remove('hidden');
    generateBtn.disabled = false;
    hideStatus();
}

// Remove selected file
function removeFile() {
    selectedFile = null;
    fileInput.value = '';
    fileInfo.classList.add('hidden');
    generateBtn.disabled = true;
    hideStatus();
}

// Upload and generate report
async function generateReport() {
    if (!selectedFile) {
        showStatus('Please select a file first', 'error');
        return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
        generateBtn.disabled = true;
        sampleBtn.disabled = true;
        hideStatus();

        // Simulate progress
        showProgress(10);
        setTimeout(() => showProgress(30), 300);
        setTimeout(() => showProgress(50), 600);

        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        showProgress(70);
        const data = await response.json();
        showProgress(90);

        if (response.ok && data.success) {
            showProgress(100);
            setTimeout(() => {
                hideProgress();
                showSuccessWithDownload();
            }, 500);
        } else {
            hideProgress();
            showStatus(data.error || 'Error generating report', 'error');
            generateBtn.disabled = false;
            sampleBtn.disabled = false;
        }
    } catch (error) {
        hideProgress();
        showStatus('Network error: ' + error.message, 'error');
        generateBtn.disabled = false;
        sampleBtn.disabled = false;
    }
}

// Generate sample report
async function generateSampleReport() {
    try {
        generateBtn.disabled = true;
        sampleBtn.disabled = true;
        hideStatus();

        // Simulate progress
        showProgress(10);
        setTimeout(() => showProgress(30), 300);
        setTimeout(() => showProgress(60), 600);

        const response = await fetch('/generate-sample');

        showProgress(85);
        const data = await response.json();
        showProgress(95);

        if (response.ok && data.success) {
            showProgress(100);
            setTimeout(() => {
                hideProgress();
                showSuccessWithDownload();
            }, 500);
        } else {
            hideProgress();
            showStatus(data.error || 'Error generating sample report', 'error');
            generateBtn.disabled = selectedFile !== null ? false : true;
            sampleBtn.disabled = false;
        }
    } catch (error) {
        hideProgress();
        showStatus('Network error: ' + error.message, 'error');
        generateBtn.disabled = selectedFile !== null ? false : true;
        sampleBtn.disabled = false;
    }
}

// Show success message with download button
function showSuccessWithDownload() {
    statusMessage.className = 'status-success';
    statusMessage.innerHTML = `
        <svg class="w-5 h-5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        <span class="flex-1">Report generated successfully!</span>
        <a href="/download-report" class="download-btn px-4 py-2 bg-white text-purple-600 rounded-lg font-semibold hover:bg-gray-100 transition-colors inline-flex items-center gap-2">
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path>
            </svg>
            Download PDF
        </a>
    `;
    statusMessage.classList.remove('hidden');

    // Reset buttons
    generateBtn.disabled = selectedFile !== null ? false : true;
    sampleBtn.disabled = false;
}

// Event Listeners
dropZone.addEventListener('click', () => fileInput.click());

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('drag-over');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('drag-over');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('drag-over');
    const file = e.dataTransfer.files[0];
    handleFileSelect(file);
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    handleFileSelect(file);
});

removeFileBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    removeFile();
});

generateBtn.addEventListener('click', generateReport);
sampleBtn.addEventListener('click', generateSampleReport);

// Keyboard shortcuts
document.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + O to open file dialog
    if ((e.ctrlKey || e.metaKey) && e.key === 'o') {
        e.preventDefault();
        fileInput.click();
    }

    // Enter to generate (if file selected)
    if (e.key === 'Enter' && selectedFile) {
        generateReport();
    }
});

// Initialize
console.log('🚀 InsightX initialized');
console.log('💡 Tip: Drag and drop your CSV file or use Ctrl+O to browse');
