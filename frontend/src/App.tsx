import React from 'react';
import { Search, MapPin, AlertTriangle, Route, Shield, BarChart3, FileText, Play } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import './App.css';

function App() {
  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-card">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center gap-3">
            <Search className="h-8 w-8 text-primary" />
            <h1 className="text-3xl font-bold text-foreground">Search 25/08/2025</h1>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {/* Visual Presentation Section */}
        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-6 text-foreground">Visual presentation of the tool:</h2>
          
          {/* Mock Interface Cards */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
            {/* Main Interface Card */}
            <Card className="bg-slate-900 text-white border-slate-700">
              <CardHeader>
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 bg-red-500 rounded-full flex items-center justify-center">
                    <MapPin className="h-4 w-4" />
                  </div>
                  <CardTitle className="text-white">Route Optimization Framework</CardTitle>
                </div>
                <CardDescription className="text-slate-300">
                  A comprehensive toolkit for building efficient and scalable route optimization applications
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  <span className="px-3 py-1 bg-blue-600 text-xs rounded-full">Real-time</span>
                  <span className="px-3 py-1 bg-green-600 text-xs rounded-full">Safety</span>
                  <span className="px-3 py-1 bg-yellow-600 text-xs rounded-full">Efficiency</span>
                  <span className="px-3 py-1 bg-purple-600 text-xs rounded-full">Analytics</span>
                  <span className="px-3 py-1 bg-red-600 text-xs rounded-full">Alerts</span>
                  <span className="px-3 py-1 bg-indigo-600 text-xs rounded-full">Monitoring</span>
                </div>
              </CardContent>
            </Card>

            {/* Quick Links Card */}
            <Card className="bg-slate-900 text-white border-slate-700">
              <CardHeader>
                <CardTitle className="text-white">Quick Links</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">Installation</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">API Docs</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">Guides</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">Build Config</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">GitHub Community</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">The Big List of Websites</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">Contributing</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">Community & Help</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">RFC</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">Team</a>
                  <a href="#" className="block text-blue-400 hover:text-blue-300 transition-colors">Blog</a>
                </div>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Description Section */}
        <section className="mb-12">
          <div className="flex items-center gap-2 mb-6">
            <Play className="h-6 w-6 text-primary" />
            <h2 className="text-2xl font-semibold text-foreground">Description</h2>
          </div>
          
          <div className="prose prose-lg max-w-none">
            <p className="text-lg text-muted-foreground mb-6">
              This project is designed to provide a <strong>web application</strong> that suggests the safest and most efficient 
              route for users by using <strong>real-time data</strong> from accidents, road conditions, and traffic information.
            </p>
            
            <p className="text-lg text-muted-foreground mb-6">
              It was built using a combination of mapping tools and real-time data APIs.
            </p>
            
            <p className="text-lg text-muted-foreground mb-8">
              The main goal of this project is to reduce the risk of accidents during the transportation of passengers 
              and cargo by enhancing route decision-making and improving driver safety.
            </p>
          </div>
        </section>

        {/* Features Section */}
        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-6 text-foreground">Key Features</h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <Route className="h-6 w-6 text-primary" />
                  <CardTitle>Intelligent Routing System</CardTitle>
                </div>
              </CardHeader>
              <CardContent>
                <CardDescription>
                  Advanced algorithms that analyze multiple factors to suggest the safest and most efficient routes.
                </CardDescription>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <AlertTriangle className="h-6 w-6 text-primary" />
                  <CardTitle>Traffic & Incident Reporting</CardTitle>
                </div>
              </CardHeader>
              <CardContent>
                <CardDescription>
                  Real-time reporting tool for traffic conditions and road incidents to keep users informed.
                </CardDescription>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <div className="flex items-center gap-2">
                  <Shield className="h-6 w-6 text-primary" />
                  <CardTitle>Safety Enhancement</CardTitle>
                </div>
              </CardHeader>
              <CardContent>
                <CardDescription>
                  Comprehensive safety features designed to reduce accident risks for both passengers and cargo.
                </CardDescription>
              </CardContent>
            </Card>
          </div>
        </section>

        {/* Installation Section */}
        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-6 text-foreground">Compile and run the project</h2>
          
          <Card>
            <CardHeader>
              <div className="flex items-center gap-2">
                <FileText className="h-6 w-6 text-primary" />
                <CardTitle>How to Run (Windows)</CardTitle>
              </div>
            </CardHeader>
            <CardContent className="space-y-4">
              <div>
                <h4 className="font-semibold mb-2">1. Setup Directory</h4>
                <p className="text-muted-foreground mb-2">
                  Create a folder named <code className="bg-muted px-2 py-1 rounded">upload</code> in the same directory as{' '}
                  <code className="bg-muted px-2 py-1 rounded">app_optimized.py</code> and place all the provided CSV files inside it.
                </p>
              </div>
              
              <div>
                <h4 className="font-semibold mb-2">2. Install Dependencies</h4>
                <div className="bg-muted p-4 rounded-lg">
                  <code>pip install -r requirements.txt</code>
                </div>
              </div>
              
              <div>
                <h4 className="font-semibold mb-2">3. Run the Application</h4>
                <div className="bg-muted p-4 rounded-lg">
                  <code>streamlit run app_optimized.py</code>
                </div>
              </div>
              
              <div>
                <h4 className="font-semibold mb-2">4. Access the Application</h4>
                <p className="text-muted-foreground">
                  Open your browser and navigate to the provided local URL.
                </p>
              </div>
            </CardContent>
          </Card>
        </section>

        {/* CTA Section */}
        <section className="text-center">
          <Card className="bg-primary/5 border-primary/20">
            <CardContent className="pt-6">
              <h3 className="text-2xl font-semibold mb-4 text-foreground">Ready to Get Started?</h3>
              <p className="text-muted-foreground mb-6">
                Follow the installation instructions above to start using the route optimization tool.
              </p>
              <Button size="lg" className="mr-4">
                <BarChart3 className="mr-2 h-4 w-4" />
                View Documentation
              </Button>
              <Button variant="outline" size="lg">
                <MapPin className="mr-2 h-4 w-4" />
                Try Demo
              </Button>
            </CardContent>
          </Card>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-border bg-card mt-16">
        <div className="container mx-auto px-4 py-8">
          <div className="text-center text-muted-foreground">
            <p>&copy; 2025 Route Optimization Tool. Built with React and TypeScript.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;

