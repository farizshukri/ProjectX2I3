const express = require('express');
const multer = require('multer');
const path = require('path');
const fetch = require('node-fetch'); // For using reverse image search API
const app = express();
const port = 3000;

// Setup multer for file uploads
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, 'uploads/');
    },
    filename: (req, file, cb) => {
        cb(null, Date.now() + path.extname(file.originalname));
    }
});
const upload = multer({ storage: storage });

app.use(express.static('public'));

// Route to handle file upload
app.post('/upload', upload.single('image'), async (req, res) => {
    if (!req.file) {
        return res.status(400).json({ error: 'No file uploaded' });
    }

    const imagePath = req.file.path;
    // Replace with your reverse image search API endpoint and key
    const apiEndpoint = 'https://api.example.com/reverse-image-search';
    const apiKey = 'YOUR_API_KEY_HERE';

    try {
        const response = await fetch(apiEndpoint, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                imagePath: imagePath
            })
        });

        const data = await response.json();

        // Send back the result
        res.json({
            imageUrl: `/${imagePath}`,
            result: data
        });
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'Server error' });
    }
});

// Serve static files
app.use(express.static('public'));

// Start server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
