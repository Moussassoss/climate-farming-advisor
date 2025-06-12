import React from 'react';
import { Cloud, Thermometer, Droplets, CloudRain, Sun, Wind, Eye, Gauge } from 'lucide-react';
import { WeatherData } from '../types';

interface WeatherCardProps {
  weather: WeatherData;
}

const WeatherCard: React.FC<WeatherCardProps> = ({ weather }) => {
  return (
    <div className="relative bg-gradient-to-br from-slate-800 via-slate-900 to-purple-900 rounded-3xl p-8 mb-8 overflow-hidden shadow-2xl border border-slate-600">
      {/* Enhanced animated background */}
      <div className="absolute inset-0 opacity-10">
        <div className="absolute top-0 right-0 w-64 h-64 bg-blue-400 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute bottom-0 left-0 w-48 h-48 bg-purple-400 rounded-full blur-3xl animate-pulse delay-1000"></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-32 h-32 bg-emerald-400 rounded-full blur-2xl animate-pulse delay-500"></div>
      </div>
      
      {/* Floating particles */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-1/4 left-1/4 w-2 h-2 bg-blue-400 rounded-full animate-float opacity-60"></div>
        <div className="absolute top-3/4 right-1/3 w-1 h-1 bg-purple-400 rounded-full animate-float delay-1000 opacity-40"></div>
        <div className="absolute top-1/2 left-3/4 w-3 h-3 bg-emerald-400 rounded-full animate-float delay-500 opacity-50"></div>
      </div>
      
      <div className="relative">
        <div className="flex items-center mb-8">
          <div className="bg-gradient-to-br from-blue-400 via-purple-500 to-indigo-600 p-4 rounded-2xl mr-4 shadow-2xl">
            <Cloud className="h-10 w-10 text-white" />
          </div>
          <div>
            <h2 className="text-3xl font-black text-white mb-1">Live Atmospheric Data</h2>
            <p className="text-blue-300 text-sm flex items-center">
              <Eye className="h-4 w-4 mr-2" />
              Real-time environmental monitoring
            </p>
          </div>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div className="group bg-gradient-to-br from-orange-500/20 to-red-500/20 backdrop-blur-sm p-6 rounded-2xl border border-orange-500/30 hover:border-orange-400/50 transition-all duration-300 hover:scale-105">
            <div className="flex items-center mb-4">
              <div className="bg-gradient-to-br from-orange-400 to-red-500 p-3 rounded-xl mr-3 shadow-lg group-hover:scale-110 transition-transform">
                <Thermometer className="h-6 w-6 text-white" />
              </div>
              <span className="text-sm font-bold text-orange-200">Temperature</span>
            </div>
            <p className="text-4xl font-black text-white mb-1">{weather.temperature}°</p>
            <p className="text-orange-300 text-xs">Celsius • Optimal Range</p>
          </div>
          
          <div className="group bg-gradient-to-br from-blue-500/20 to-cyan-500/20 backdrop-blur-sm p-6 rounded-2xl border border-blue-500/30 hover:border-blue-400/50 transition-all duration-300 hover:scale-105">
            <div className="flex items-center mb-4">
              <div className="bg-gradient-to-br from-blue-400 to-cyan-500 p-3 rounded-xl mr-3 shadow-lg group-hover:scale-110 transition-transform">
                <Droplets className="h-6 w-6 text-white" />
              </div>
              <span className="text-sm font-bold text-blue-200">Humidity</span>
            </div>
            <p className="text-4xl font-black text-white mb-1">{weather.humidity}%</p>
            <p className="text-blue-300 text-xs">Relative • Air Moisture</p>
          </div>
          
          <div className="group bg-gradient-to-br from-cyan-500/20 to-teal-500/20 backdrop-blur-sm p-6 rounded-2xl border border-cyan-500/30 hover:border-cyan-400/50 transition-all duration-300 hover:scale-105">
            <div className="flex items-center mb-4">
              <div className="bg-gradient-to-br from-cyan-400 to-teal-500 p-3 rounded-xl mr-3 shadow-lg group-hover:scale-110 transition-transform">
                <CloudRain className="h-6 w-6 text-white" />
              </div>
              <span className="text-sm font-bold text-cyan-200">Precipitation</span>
            </div>
            <p className="text-4xl font-black text-white mb-1">{weather.rain}</p>
            <p className="text-cyan-300 text-xs">mm • Recent Rainfall</p>
          </div>
          
          <div className="group bg-gradient-to-br from-purple-500/20 to-indigo-500/20 backdrop-blur-sm p-6 rounded-2xl border border-purple-500/30 hover:border-purple-400/50 transition-all duration-300 hover:scale-105">
            <div className="flex items-center mb-4">
              <div className="bg-gradient-to-br from-purple-400 to-indigo-500 p-3 rounded-xl mr-3 shadow-lg group-hover:scale-110 transition-transform">
                <Sun className="h-6 w-6 text-white" />
              </div>
              <span className="text-sm font-bold text-purple-200">Sky Conditions</span>
            </div>
            <p className="text-lg font-bold text-white capitalize leading-tight mb-1">
              {weather.sky_description}
            </p>
            <p className="text-purple-300 text-xs">Current • Visibility</p>
          </div>
        </div>
        
        {/* Enhanced status indicator */}
        <div className="mt-6 bg-gradient-to-r from-emerald-500/10 to-blue-500/10 backdrop-blur-sm rounded-2xl p-4 border border-emerald-500/20">
          <div className="flex items-center justify-center">
            <div className="flex items-center space-x-3">
              <div className="w-3 h-3 bg-emerald-400 rounded-full animate-pulse"></div>
              <span className="text-emerald-300 font-medium text-sm">Live Data Stream Active</span>
              <Gauge className="h-4 w-4 text-emerald-400" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WeatherCard;