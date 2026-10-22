class Bank {
    private long[] balance;

    public Bank(long[] balance) {
        this.balance = balance;
    }
    
    public boolean transfer(int account1, int account2, long money) {
        if (!accountInBounds(account1)) return false;
        if (!accountInBounds(account2)) return false;
        if (!this.withdraw(account1, money)) return false;
        return this.deposit(account2, money);
    }
    
    public boolean deposit(int account, long money) {
        if (!accountInBounds(account)) return false;
        this.balance[account-1] += money;
        return true;
    }
    
    public boolean withdraw(int account, long money) {
        if (!accountInBounds(account)) return false;
        if (!(this.balance[account-1] >= money)) return false;
        this.balance[account-1] -= money;
        return true;
    }

    private boolean accountInBounds(int account) {
        return 1 <= account && account <= this.balance.length;
    }
}

/**
 * Your Bank object will be instantiated and called as such:
 * Bank obj = new Bank(balance);
 * boolean param_1 = obj.transfer(account1,account2,money);
 * boolean param_2 = obj.deposit(account,money);
 * boolean param_3 = obj.withdraw(account,money);
 */