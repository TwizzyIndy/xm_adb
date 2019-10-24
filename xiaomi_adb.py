from adb_functions import AdbFunctions
import os


def usage():
    
    print("")
    print("")
    print("Xiaomi ADB for MiRecovery")
    print("by TwizzyIndy")
    print("10/2018")
    print("")
    print("usage     : python xiaomi_adb.py [arguments] ")
    print("")
    print(" -fd      : format data ")
    print(" -fs      : format storage")
    print(" -fds     : format data and storage")
    print(" -wds     : wipe data and storage")
    print(" -r       : reboot")
    print(" -redl    : reboot to edl")
    print(" -rrec    : reboot to recovery")
    print(" -rbl     : reboot to bootlaoder")
    print(" -info    : get device infos")
    print(" -shut    : shutdown")
    print(" -clearefs: wipe efs")
    print(" -mtp_on  : mtp mode on")
    print(" -mtp_off : mtp mode off")
    print(" -getdump : get dump")
    print(" -mtp_install_apk : install apk from mtp enabled recovery mode")
    print("")
    return

def sendAdbCommand(cmd):
    
    adb = AdbFunctions()
    adb_devices = adb.devices()
    
    if not adb_devices:
        print("no devices found")

    if cmd == '-r':
        print(adb.command('reboot:'))
        
    elif cmd == '-rrec':
        print(adb.command('reboot:recovery'))
        
    elif cmd == '-redl':
        print(adb.command('reboot:edl'))
    elif cmd == '-rbl':
        print(adb.command('reboot:bootloader'))
        
    elif cmd == '-shut':
        print(adb.command('shutdown:'))
    elif cmd == '-info':
        
        print("")
        print("Device : " + str(adb.queryCommand('getdevice:')))
        print("Version: " + str(adb.queryCommand('getversion:')))
        print("Codebase: " + str(adb.queryCommand('getcodebase:')))
        print("Region: " + str(adb.queryCommand('getregion:')))
        print("Branch: " + str(adb.queryCommand('getbranch:')))
        print("Language: "+ str(adb.queryCommand('getlanguage:')))
        print("Serial: " + str(adb.queryCommand('getsn:')))
        print("RomZone: " + str(adb.queryCommand('getromzone:')))
        print("RecoveryVersion: " + str(adb.queryCommand('getrecoveryversion:')))
        
    elif cmd == '-fd':
        
        print( adb.command('format-data:'))
        
    elif cmd == '-fs':
        print( adb.command('format-storage:'))
        
    elif cmd == '-fds':
        print( adb.command('format-data-storage:'))
    
    elif cmd == '-wds':
        print( adb.command('wipe-data-storage:'))
        
        
    elif cmd == '-clearefs':
        print( adb.command('wipe-efs:'))
        
    elif cmd == '-mtp_on': # need to test query or command type
        print( adb.command('enablemtp:'))
    elif cmd == '-mtp_off':
        print( adb.command('disablemtp:'))
    elif cmd == '-getdump':
        print( adb.command('getminidump'))
        
    else:
        usage()
        
    return

def main():
    
    if( len(os.sys.argv) < 2 ):
        usage()
        return
    
    arg = os.sys.argv[1]
    
    sendAdbCommand(arg)
    

    return


if __name__ == "__main__":
    main()