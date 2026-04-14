import { useState } from 'react'
import SearchBar from './components/SearchBar'
import SearchArt from './api'
import Gallery from './components/Gallery'

function App() {
  const [artwork, setArtwork] = useState([])

  const handleSearch = async(query) =>{
    const data = await SearchArt(query)
    setArtwork(data)
  }

  return (
    <div>
      <h1>AI-Powered Art Search</h1>
      <SearchBar onSubmit={handleSearch} />
      <Gallery artwork={artwork}/>
    </div>
  )
    
}

export default App
