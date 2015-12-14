package com.nourriture.app.setting;

import android.content.Intent;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import com.nourriture.app.R;

/**
 * Created by liuyifan on 15/12/15.
 */
public class PersonalSettingPasswordFragment extends Fragment {
    private View view;
    private String password;
    boolean isTwoPane;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //get password and isTwoPane from Bundle--tablet or Intent--phone
        if (getArguments()!=null && getArguments().containsKey("password") && getArguments().containsKey("isTwoPane")) {
            password = getArguments().getString("password");
            isTwoPane = getArguments().getBoolean("isTwoPane");
        } else if (getActivity().getIntent().getStringExtra("password") != null) {
            password = getActivity().getIntent().getStringExtra("password");
            isTwoPane = getActivity().getIntent().getBooleanExtra("isTwoPane", false);
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        view = inflater.inflate(R.layout.setting_password_frag, container, false);

        Button button = (Button) view.findViewById(R.id.password_submit);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view1) {
                EditText pass1 = (EditText) view.findViewById(R.id.edit_password1);
                EditText pass2 = (EditText) view.findViewById(R.id.edit_password2);
                String new_pass1 = pass1.getText().toString();
                String new_pass2 = pass2.getText().toString();

                if (!new_pass1.equals(new_pass2)){
                    // notify something--different <TODO>
                } else if (new_pass1.equals(password)) {
                    // notify something--no changes <TODO>
                } else {
                    if (isTwoPane) {
                        // refresh the value of password in the left fragment
                        PersonalSettingFragment personalSettingFragment = (PersonalSettingFragment)
                                getActivity().getSupportFragmentManager().getFragments().get(0); //maybe there is a better way to get the fragmant
                        personalSettingFragment.changeValue(2, new_pass1);
                    } else {
                        // return the value of password to PersonalSettingFragment
                        Intent intent = getActivity().getIntent();
                        intent.putExtra("password", new_pass1);
                        getActivity().setResult(2, intent);
                        getActivity().finish();
                    }
                    password = new_pass1;
                }
            }
        });
        return view;
    }
}
